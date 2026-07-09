#!/usr/bin/env bash
# Regenerate the graphiant-sdk-python from the OpenAPI specification.
#
# Prerequisites:
#   - Java 11+ on PATH
#   - openapi-generator-cli (install via: brew install openapi-generator
#     or: npm install @openapitools/openapi-generator-cli -g)
#
# Usage:
#   bash scripts/generate.sh                    # uses api/openapi.yaml
#   OPENAPI_SPEC=api/graphiant_api_docs_v26.6.0.json bash scripts/generate.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Resolve default spec: prefer api/openapi.yaml (canonical), fall back to the
# versioned JSON bundle (api/graphiant_api_docs_*.json) if yaml is absent.
if [ -z "${OPENAPI_SPEC:-}" ]; then
  if [ -f "${REPO_ROOT}/api/openapi.yaml" ]; then
    OPENAPI_SPEC="${REPO_ROOT}/api/openapi.yaml"
  else
    OPENAPI_SPEC="$(ls "${REPO_ROOT}"/api/graphiant_api_docs_*.json 2>/dev/null | sort | tail -1)"
  fi
fi

PACKAGE_NAME="${PACKAGE_NAME:-graphiant_sdk}"

# Read SDK version from pyproject.toml so generated docs/UserAgent stay correct.
SDK_VERSION=$(grep -E '^version\s*=' "${REPO_ROOT}/pyproject.toml" | head -1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')

# Resolve generator: honour explicit $GENERATOR, then try common install locations.
if [ -n "${GENERATOR:-}" ]; then
  : # use what was passed
elif command -v openapi-generator &>/dev/null; then
  GENERATOR="openapi-generator"          # Homebrew: brew install openapi-generator
elif command -v openapi-generator-cli &>/dev/null; then
  GENERATOR="openapi-generator-cli"      # npm: npm i -g @openapitools/openapi-generator-cli
else
  echo "❌ openapi-generator not found. Install via one of:"
  echo "   brew install openapi-generator          # macOS Homebrew"
  echo "   npm install -g @openapitools/openapi-generator-cli"
  echo "   https://openapi-generator.tech/docs/installation"
  exit 1
fi

if [ ! -f "${OPENAPI_SPEC}" ]; then
  echo "❌ OpenAPI spec not found: ${OPENAPI_SPEC}"
  exit 1
fi

echo "🔄 Generating SDK v${SDK_VERSION} from ${OPENAPI_SPEC}..."

"${GENERATOR}" generate \
  --input-spec "${OPENAPI_SPEC}" \
  --generator-name python \
  --output "${REPO_ROOT}" \
  --git-user-id Graphiant-Inc \
  --git-repo-id graphiant-sdk-python \
  --additional-properties="packageName=${PACKAGE_NAME},projectName=graphiant-sdk,packageVersion=${SDK_VERSION},generateSourceCodeOnly=false"

echo "🔧 Reinstalling package..."
cd "${REPO_ROOT}"
pip install -e ".[dev]" --quiet 2>/dev/null || pip install -e . --quiet

echo "✅ SDK generation complete."
echo "   Files listed in .openapi-generator-ignore are NOT overwritten, including:"
echo "   - graphiant_cli/  (hand-written CLI)"
echo "   - graphiant_sdk/api_client.py, configuration.py, exceptions.py, rest.py, api_response.py"
echo "   Review the diff before committing."
