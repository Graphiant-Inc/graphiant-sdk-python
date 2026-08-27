#!/usr/bin/env bash
# Compare two versions of the OpenAPI spec with oasdiff (breaking-change check or full changelog).
#
# Requires Docker.
#
# Usage:
#   bash scripts/oasdiff.sh                            # breaking-change report: prev spec vs latest spec
#   MODE=changelog bash scripts/oasdiff.sh              # full markdown changelog instead
#   bash scripts/oasdiff.sh api/old.json api/new.json   # diff two explicit spec files
#
# Auto-detection (no args):
#   - If two or more api/graphiant_api_docs_v*.json files are present locally (e.g. you just
#     dropped a new spec in alongside the old one), diffs the two highest versions.
#   - Otherwise diffs the latest local spec against the version committed on $BASE_REF
#     (default: origin/main).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

MODE="${MODE:-breaking}"
BASE_REF="${BASE_REF:-origin/main}"
CLEANUP=""

if [ "$#" -eq 2 ]; then
  BASE_SPEC="$1"
  HEAD_SPEC="$2"
else
  HEAD_SPEC="$(ls api/graphiant_api_docs_v*.json 2>/dev/null | sort -V | tail -1 || true)"
  if [ -z "${HEAD_SPEC:-}" ]; then
    echo "❌ No api/graphiant_api_docs_v*.json found." >&2
    exit 1
  fi

  LOCAL_SPEC_COUNT="$(ls api/graphiant_api_docs_v*.json 2>/dev/null | wc -l | tr -d ' ')"
  if [ "$LOCAL_SPEC_COUNT" -ge 2 ]; then
    BASE_SPEC="$(ls api/graphiant_api_docs_v*.json | sort -V | tail -2 | head -1)"
  else
    BASE_SPEC_NAME="$(git ls-tree -r --name-only "$BASE_REF" -- api 2>/dev/null | grep -E '^api/graphiant_api_docs_v[0-9.]+\.json$' | sort -V | tail -1 || true)"
    if [ -z "$BASE_SPEC_NAME" ]; then
      echo "❌ Could not find a previous spec on ${BASE_REF} to diff against. Pass two spec files explicitly." >&2
      exit 1
    fi
    BASE_SPEC="api/.oasdiff-base.json"
    git show "${BASE_REF}:${BASE_SPEC_NAME}" > "$BASE_SPEC"
    CLEANUP="$BASE_SPEC"
  fi
fi

[ -n "$CLEANUP" ] && trap 'rm -f "$CLEANUP"' EXIT

if ! command -v docker &>/dev/null; then
  echo "❌ Docker not found. oasdiff runs via the tufin/oasdiff Docker image: https://github.com/oasdiff/oasdiff" >&2
  exit 1
fi

FORMAT="text"
[ "$MODE" = "changelog" ] && FORMAT="markdown"

echo "🔍 oasdiff ${MODE}: ${BASE_SPEC} → ${HEAD_SPEC}"
echo
docker run --rm -t --mount "type=bind,src=${REPO_ROOT},dst=/data" tufin/oasdiff "${MODE}" \
  --format "${FORMAT}" \
  "/data/${BASE_SPEC}" \
  "/data/${HEAD_SPEC}"
