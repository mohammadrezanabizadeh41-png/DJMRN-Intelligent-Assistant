#!/usr/bin/env bash
# DJMRN P2C, one manual-only GitHub Actions run. No user data or real provider APIs.
set -Eeuo pipefail

if [[ "${DJMRN_APPROVED_FREE_ACTIONS_MINUTES:-}" != 'yes' ]]; then
  echo 'STOP: free public-repository standard-runner approval is required.'
  exit 90
fi
if [[ "$(uname -s)" != 'Linux' || "$(uname -m)" != 'x86_64' ]]; then
  echo 'STOP: requires isolated linux/amd64 GitHub-hosted runner'
  exit 91
fi
command -v docker >/dev/null || { echo 'STOP: Docker not installed'; exit 92; }
command -v python3 >/dev/null || { echo 'STOP: Python 3 not installed'; exit 93; }
command -v curl >/dev/null || { echo 'STOP: curl is not installed'; exit 93; }
command -v git >/dev/null || { echo 'STOP: git is not installed'; exit 93; }

HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
NETWORK="djmrn-p2c-${GITHUB_RUN_ID:-manual}-$$"
BIN="maximhq/bifrost@sha256:d53775fd4b1d444c350443d2487ceb8aa8c0bab722cd5dc7b0001a7fa88ecd7f"

FIXTURES="$(mktemp -d -t djmrn-p2c.XXXXXXXX)"
A='djmrn-mock-a'
B='djmrn-mock-b'
GATE='djmrn-bifrost-p2c'

cleanup() {
  docker rm -f "$GATE" "$A" "$B" >/dev/null 2>&1 || true
  docker network rm "$NETWORK" >/dev/null 2>&1 || true
  rm -rf -- "$FIXTURES"
  echo 'DJMRN P2C ephemeral containers/network cleanup completed'
}
trap cleanup EXIT

VENDOR_SOURCE_COMMIT='a05ea20e68bf116a35e9f05b1a3d749624b3935e'
for entry in \
  'pricing.json b12642f6808eca16adfdcf6dcdf656e3f145bcf7' \
  'model-parameters.json 31532d0f1f48af3ddd0a916543f36ccc367b7e00'; do
  read -r filename blob <<< "$entry"
  url="https://raw.githubusercontent.com/maximhq/bifrost/${VENDOR_SOURCE_COMMIT}/examples/configs/withlocalpricingfiles/${filename}"
  curl --proto '=https' --tlsv1.2 -fLsS --max-time 30 --retry 1 --output "$FIXTURES/$filename" "$url"
  if [[ "$(git hash-object -- "$FIXTURES/$filename")" != "$blob" ]]; then echo "STOP: vendor Git blob mismatch: $filename"; exit 98; fi
done

echo 'Checking pinned official linux/amd64 OCI image (no latest tag).'
docker pull --platform linux/amd64 "$BIN" >/dev/null
docker pull python:3.13-slim >/dev/null
INSPECT="$(docker image inspect --format '{{.Os}}/{{.Architecture}}' "$BIN")"
[[ "$INSPECT" == 'linux/amd64' ]] || { echo "STOP: unexpected image arch: $INSPECT"; exit 94; }
# The image identity is enforced by the digest-qualified pull above.

docker network create --driver bridge --internal "$NETWORK" >/dev/null
[[ "$(docker network inspect --format '{{.Internal}}' "$NETWORK")" == 'true' ]] || {
  echo 'STOP: network has external routing'; exit 95;
}

export BIFROST_ADMIN_USERNAME='djmrn-test-admin'
export BIFROST_ADMIN_PASSWORD="$(python3 -c 'import secrets;print(secrets.token_urlsafe(32))')"
export BIFROST_SETUP_TOKEN="$(python3 -c 'import secrets;print(secrets.token_hex(32))')"
export BIFROST_TEST_VIRTUAL_KEY="sk-bf-$(python3 -c 'import secrets;print(secrets.token_hex(24))')"
export DJMRN_FAKE_PROVIDER_TOKEN='SYNTHETIC-NOT-AN-API-KEY'
# Mask ephemeral values in GitHub logs, including accidental nested command traces.
for val in "$BIFROST_ADMIN_PASSWORD" "$BIFROST_SETUP_TOKEN" "$BIFROST_TEST_VIRTUAL_KEY"; do
  printf '::add-mask::%s\n' "$val"
done

for item in 'A djmrn-mock-a' 'B djmrn-mock-b'; do
  read -r name container <<< "$item"
  docker run --detach --rm --name "$container" --network "$NETWORK" \
    --cap-drop ALL --security-opt no-new-privileges --memory 256m \
    -e "DJMRN_MOCK_NAME=$name" \
    --mount "type=bind,source=$HERE/mock_provider.py,target=/opt/mock_provider.py,readonly" \
    python:3.13-slim python -u /opt/mock_provider.py >/dev/null
done

echo 'Launching digest-pinned actual Maxim Bifrost with fake providers and no external container egress.'
docker run --detach --name "$GATE" --network "$NETWORK" \
  --cap-drop ALL --security-opt no-new-privileges --memory 1536m --cpus 2 \
  --tmpfs '/tmp:rw,nosuid,nodev,size=64m,uid=1000,gid=0' \
  -e APP_HOST=0.0.0.0 \
  -e BIFROST_SETUP_TOKEN -e BIFROST_ADMIN_USERNAME -e BIFROST_ADMIN_PASSWORD \
  -e BIFROST_TEST_VIRTUAL_KEY -e DJMRN_FAKE_PROVIDER_TOKEN \
  --mount "type=bind,source=$HERE/config.json,target=/app/data/config.json,readonly" \
  --mount "type=bind,source=$FIXTURES/pricing.json,target=/app/data/pricing.json,readonly" \
  --mount "type=bind,source=$FIXTURES/model-parameters.json,target=/app/data/model-parameters.json,readonly" \
  "$BIN" >/dev/null

# Probe from a separate ephemeral client within the internal-only Docker network.
if ! docker run --rm --network "$NETWORK" --cap-drop ALL --security-opt no-new-privileges --memory 256m \
  -e DJMRN_GATEWAY_TEST_URL="http://$GATE:8080/v1/chat/completions" \
  -e BIFROST_ADMIN_USERNAME -e BIFROST_ADMIN_PASSWORD -e BIFROST_TEST_VIRTUAL_KEY \
  --mount "type=bind,source=$HERE/probe_gateway.py,target=/opt/probe_gateway.py,readonly" \
  python:3.13-slim python -u /opt/probe_gateway.py; then
  echo 'P2C_GATEWAY_PROBE_FAILED: inspect state and scrubbed startup errors; NOT PASS'
  docker inspect --format 'docker_state={{.State.Status}} exit_code={{.State.ExitCode}} oom_killed={{.State.OOMKilled}}' "$GATE" 2>/dev/null || true
  python3 - <<'PYSANITIZE' || true
import os, subprocess, re
p=subprocess.run(['docker','logs','--tail','40','djmrn-bifrost-p2c'],capture_output=True,text=True)
lines=(p.stdout+'\n'+p.stderr).splitlines()
for v in [os.getenv(k,'') for k in ('BIFROST_ADMIN_PASSWORD','BIFROST_SETUP_TOKEN','BIFROST_TEST_VIRTUAL_KEY','DJMRN_FAKE_PROVIDER_TOKEN')]:
    if v: lines=[line.replace(v,'[REDACTED]') for line in lines]
for line in lines[-24:]:
    if any(term in line.lower() for term in ('error','fatal','panic','invalid','config','failed','permission','startup','server','sqlite','virtual','pricing')):
        print('DIAGNOSTIC: '+re.sub(r'sk-bf-[a-zA-Z0-9_-]+','[REDACTED-VK]',line)[:450])
PYSANITIZE
  exit 96
fi
echo 'P2C_GATEWAY_PROBE_SCRIPT_COMPLETED (see individual printed probes; not provider quota or Windows proof)'
if [[ "${DJMRN_P2E_SYNTHETIC_INTEGRATION:-}" == 'yes' ]]; then
  P2D_DIR="$HERE/../ROUTER-P002D-20261023"
  P2E_DIR="$HERE/../ROUTER-P002E-20261023"
  for needed in "$P2D_DIR/admission.py" "$P2E_DIR/integration.py"; do
    [[ -f "$needed" ]] || { echo 'STOP: missing P2E source'; exit 97; }
  done
  echo 'Launching P2E integrated metered-admission probe: only fake upstreams.'
  docker run --rm --network "$NETWORK" --cap-drop ALL --security-opt no-new-privileges \
    --memory 256m \
    -e DJMRN_P2E_SYNTHETIC_ONLY=yes \
    -e DJMRN_GATEWAY_TEST_URL="http://$GATE:8080/v1/chat/completions" \
    -e BIFROST_ADMIN_USERNAME -e BIFROST_ADMIN_PASSWORD -e BIFROST_TEST_VIRTUAL_KEY \
    --mount "type=bind,source=$P2D_DIR,target=/opt/ROUTER-P002D-20261023,readonly" \
    --mount "type=bind,source=$P2E_DIR,target=/opt/ROUTER-P002E-20261023,readonly" \
    python:3.13-slim python -u /opt/ROUTER-P002E-20261023/integration.py
  echo 'P2E_ADMITTED_GENUINE_BIFROST_SYNTHETIC_PROBE_COMPLETED'
fi
