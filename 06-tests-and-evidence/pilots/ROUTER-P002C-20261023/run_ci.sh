#!/usr/bin/env bash
# DJMRN P2C, one manual-only GitHub Actions run. No user data or real provider APIs.
set -Eeuo pipefail

if [[ "${DJMRN_APPROVED_FREE_ACTIONS_MINUTES:-}" != 'yes' ]]; then
  echo 'STOP: account owner must verify available free Actions minutes and a zero-overage spending budget before manually dispatching.'
  exit 90
fi
if [[ "$(uname -s)" != 'Linux' || "$(uname -m)" != 'x86_64' ]]; then
  echo 'STOP: requires isolated linux/amd64 GitHub-hosted runner'
  exit 91
fi
command -v docker >/dev/null || { echo 'STOP: Docker not installed'; exit 92; }
command -v python3 >/dev/null || { echo 'STOP: Python 3 not installed'; exit 93; }

HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
NETWORK="djmrn-p2c-${GITHUB_RUN_ID:-manual}-$$"
BIN="maximhq/bifrost@sha256:d53775fd4b1d444c350443d2487ceb8aa8c0bab722cd5dc7b0001a7fa88ecd7f"
A='djmrn-mock-a'
B='djmrn-mock-b'
GATE='djmrn-bifrost-p2c'

cleanup() {
  docker rm -f "$GATE" "$A" "$B" >/dev/null 2>&1 || true
  docker network rm "$NETWORK" >/dev/null 2>&1 || true
  echo 'DJMRN P2C ephemeral containers/network cleanup completed'
}
trap cleanup EXIT

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
docker run --detach --rm --name "$GATE" --network "$NETWORK" \
  --publish 127.0.0.1:18080:8080 \
  --cap-drop ALL --security-opt no-new-privileges --memory 1536m --cpus 2 \
  -e APP_HOST=0.0.0.0 \
  -e BIFROST_SETUP_TOKEN -e BIFROST_ADMIN_USERNAME -e BIFROST_ADMIN_PASSWORD \
  -e BIFROST_TEST_VIRTUAL_KEY -e DJMRN_FAKE_PROVIDER_TOKEN \
  --mount "type=bind,source=$HERE/config.json,target=/app/data/config.json,readonly" \
  "$BIN" >/dev/null

STATUS='NOT_READY'
for _ in $(seq 1 45); do
  if curl -sf --connect-timeout 2 --max-time 2 'http://127.0.0.1:18080/health' >/dev/null; then STATUS='READY'; break; fi
  sleep 1
done
[[ "$STATUS" == 'READY' ]] || { echo 'BLOCKED: pinned Bifrost container did not answer /health; no PASS claimed'; exit 96; }

python3 "$HERE/probe_gateway.py"
echo 'P2C_GATEWAY_PROBE_SCRIPT_COMPLETED (see individual printed probes; not provider quota or Windows proof)'
