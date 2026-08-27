# Contributing to Graphiant SDK Python

Thank you for your interest in contributing!

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork:**
   ```bash
   git clone https://github.com/Graphiant-Inc/graphiant-sdk-python.git
   cd graphiant-sdk-python
   ```
3. **Set up development environment:**
   ```bash
   python3 -m venv venv && source venv/bin/activate
   make install        # pip install -e ".[dev]"
   ```

## Development Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and ensure they pass local checks:
   ```bash
   make test           # pytest --cov=graphiant_sdk ...
   make lint           # flake8 on hand-written files (generated excluded via .flake8)
   make type-check     # mypy (generated models excluded via pyproject.toml)
   make build          # python -m build (wheel + sdist)

   # Or individually:
   pytest -v tests/
   flake8 graphiant_cli/ graphiant_sdk/api_client.py graphiant_sdk/configuration.py ...
   mypy graphiant_sdk/ graphiant_cli/
   ```

3. **Commit with clear messages:**
   ```bash
   git commit -m "Add: description of changes"
   ```
   
   **Note**: All commits must be signed with GPG. See [Branch Protection Requirements](#branch-protection-requirements) below.

5. **Push and create a pull request**

## Linting Tools

The project uses multiple linting tools to ensure code quality:

| Tool | Purpose | Target | CI/CD |
|------|---------|--------|-------|
| `flake8` | Python style guide (PEP 8) | Hand-written files only (`.flake8` excludes generated models) | Yes (lint stage) |
| `mypy` | Static type checking | Hand-written files (generated models excluded via `pyproject.toml`) | Yes (lint stage) |

Generated files (`graphiant_sdk/models/`, `default_api.py`, `__init__.py`) are excluded from linting and type-checking. Run `make lint` and `make type-check` locally to verify.

**Note:** All linting tools run automatically in CI/CD on every pull request and push to main/develop branches.

## Testing

### Running Tests Locally

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest -v tests/

# Run with coverage
pytest --cov=graphiant_sdk --cov-report=html tests/

# Run specific test file
pytest tests/test_default_api.py

# Run specific test
pytest tests/test_default_api.py::test_function_name
```

### Test Structure

- `tests/` directory contains all test files (hand-written; listed in `.openapi-generator-ignore`)
- Tests use the `pytest` framework
- Tests are automatically run in CI/CD across Python 3.10, 3.11, 3.12, and 3.13

### Writing Tests

```python
import pytest
from graphiant_sdk import ApiClient, Configuration
from graphiant_sdk.exceptions import ApiException

def test_example():
    """Test example with proper docstring"""
    config = Configuration(host="https://api.graphiant.com")
    client = ApiClient(config)
    
    # Test implementation
    assert client is not None

def test_error_handling():
    """Test error handling"""
    with pytest.raises(ApiException):
        # Code that should raise ApiException
        pass
```

## Code Generation

Most files in this repo (`graphiant_sdk/models/`, `graphiant_sdk/api/default_api.py`, `graphiant_sdk/__init__.py`, `docs/`) are auto-generated from the OpenAPI spec. **Do not edit them directly** — your changes will be overwritten on the next generation run.

The hand-written files are protected by `.openapi-generator-ignore`:
- `graphiant_cli/` — entire CLI package
- `graphiant_sdk/api_client.py`, `configuration.py`, `exceptions.py`, `rest.py`, `api_response.py`, `py.typed`
- `tests/` — all tests
- `pyproject.toml`, `setup.py`, `requirements.txt`, `README.md`, `CHANGELOG.md`, tooling files

To regenerate after a spec update:

```bash
# Place the new spec in api/ then:
make generate
# or: OPENAPI_SPEC=api/my-new-spec.json bash scripts/generate.sh
```

`scripts/generate.sh` auto-detects `openapi-generator` (Homebrew) or `openapi-generator-cli` (npm), reads `packageVersion` from `pyproject.toml`, and passes `--git-user-id`/`--git-repo-id` so generated docs never contain `GIT_USER_ID` placeholders.

Review `git diff` carefully after generation — pay particular attention to files in `.openapi-generator-ignore` to confirm they were not overwritten.

### Checking for breaking API changes (oasdiff)

Any PR that touches `api/graphiant_api_docs_*.json` automatically gets an [oasdiff](https://github.com/oasdiff/oasdiff) breaking-change report — a job summary and inline annotations on the spec file from `OpenAPI Diff (oasdiff)` (`.github/workflows/oasdiff.yml`), plus a sticky PR comment (updated in place on each push, not duplicated) from a follow-up job, `OpenAPI Diff Comment` (`.github/workflows/oasdiff-comment.yml`). That job is split out and triggered via `workflow_run` specifically so it can safely get a write-capable token for PRs from forks, without ever needing to check out or execute anything from the PR itself — see the comments in that file for the reasoning. No need to run any of this manually before opening a PR, but you can reproduce it locally while drafting the `CHANGELOG.md` entry:

```bash
make oasdiff             # breaking-change report
make oasdiff-changelog   # full markdown changelog of every spec change
```

Requires Docker (pulls `tufin/oasdiff`). By default it diffs the two highest-versioned specs found in `api/` if you've dropped a new one in alongside the old one, otherwise the latest local spec against the version committed on `origin/main`.

The CI check is informational, not a merge gate — the Graphiant API doesn't follow strict semver, so a spec bump can legitimately include breaking changes. If oasdiff flags something, call it out explicitly in the PR description and `CHANGELOG.md` entry rather than silently letting the generated SDK diff speak for itself.

## Code Standards

### Python Code
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use type hints for all function signatures
- Include docstrings for all classes, functions, and modules
- Keep functions focused and small
- Use meaningful variable and function names
- Handle exceptions explicitly

### Type Hints

```python
from typing import List, Optional, Dict
from graphiant_sdk.models import V1EdgesSummaryGetResponse

def get_devices(
    api_client: ApiClient,
    bearer_token: str
) -> Optional[V1EdgesSummaryGetResponse]:
    """
    Get list of devices.
    
    Args:
        api_client: The API client instance
        bearer_token: Authentication bearer token
        
    Returns:
        Device summary response or None if error
    """
    # implementation
    pass
```

### Docstrings

Use Google-style docstrings:

```python
def configure_device(
    device_id: int,
    config: Dict[str, Any]
) -> bool:
    """
    Configure a device with the given configuration.
    
    Args:
        device_id: The ID of the device to configure
        config: Configuration dictionary
        
    Returns:
        True if configuration was successful, False otherwise
        
    Raises:
        ApiException: If the API request fails
    """
    # implementation
    pass
```

### Example Code Structure

```python
"""
Module docstring describing the module's purpose.
"""
from typing import Optional
from graphiant_sdk import ApiClient, Configuration
from graphiant_sdk.exceptions import ApiException

class DeviceManager:
    """
    Manager class for device operations.
    """
    
    def __init__(self, api_client: ApiClient):
        """
        Initialize the device manager.
        
        Args:
            api_client: The API client instance
        """
        self.api_client = api_client
    
    def get_device(self, device_id: int) -> Optional[dict]:
        """
        Get device information.
        
        Args:
            device_id: The device ID
            
        Returns:
            Device information dictionary or None
        """
        # implementation
        pass
```

## Pull Request Checklist

- [ ] `make test` passes (all tests green)
- [ ] `make lint` passes (no new flake8 errors in hand-written files)
- [ ] `make type-check` passes (no new mypy errors)
- [ ] `make build` succeeds (wheel and sdist build cleanly)
- [ ] If adding/changing generated code: `make generate` was run and only expected files changed
- [ ] Type hints included for all new functions
- [ ] Commit messages are clear
- [ ] Commits are signed with GPG (required)
- [ ] Branch is rebased (no merge commits allowed)
- [ ] All CI/CD checks pass (lint, test, build)

## Branch Protection Requirements

This repository has branch protection rules that must be satisfied before a pull request can be merged:

### Required Approvals
- **SRE Team Approval**: All pull requests require approval from `@Graphiant-Inc/sre`
- **Code Owners**: Additional approvals may be required based on CODEOWNERS file

### Merge Requirements
- **Merge Method**: Only **squash merge** or **rebase merge** are allowed (standard merge is disabled)
- **No Merge Commits**: Your branch must not contain merge commits
  - Use `git rebase` instead of `git merge` when updating your branch
  - Example: `git pull --rebase origin main` or `git rebase origin/main`

### Commit Requirements
- **Signed Commits**: All commits must be verified with GPG signatures
  - Set up GPG signing: https://docs.github.com/en/authentication/managing-commit-signature-verification
  - Configure Git: `git config --global commit.gpgsign true`
  - Verify your commits are signed: `git log --show-signature`

### CI/CD Requirements
- **All Checks Must Pass**: All lint, test, and build workflows must pass
- **No Skipped Tests**: All tests must run and pass
- **Coverage**: Maintain or improve test coverage

## Troubleshooting

### GPG Signing Issues

If you encounter "gpg failed to sign the data":
1. Ensure GPG is installed and configured
2. Set `GPG_TTY`: `export GPG_TTY=$(tty)`
3. Verify your key: `gpg --list-secret-keys --keyid-format LONG`
4. Configure Git: `git config --global user.signingkey YOUR_KEY_ID`

If you encounter "The email in this signature doesn't match the committer email":
1. Ensure your commit author email matches your GPG key email
2. Amend the commit: `GIT_COMMITTER_EMAIL="your-email@example.com" git commit --amend --author="Your Name <your-email@example.com>" --no-edit -S`

### Virtual Environment Issues

If you encounter import errors:
1. Ensure virtual environment is activated: `source venv/bin/activate`
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Verify installation: `pip list | grep graphiant-sdk`

### Linting Issues

If `flake8` or `mypy` fail:
1. Run with verbose output: `flake8 --verbose graphiant_sdk/`
2. Check specific errors: `mypy graphiant_sdk/ --show-error-codes`
3. Auto-fix some issues: `autopep8 --in-place --recursive graphiant_sdk/`

### Test Failures

If tests fail:
1. Run with verbose output: `pytest -v tests/`
2. Run specific test: `pytest tests/test_file.py::test_function -v`
3. Check test coverage: `pytest --cov=graphiant_sdk --cov-report=term tests/`

### Unexpected model changes after `make generate`

`openapi-generator` deduplicates inline anonymous response schemas (e.g. simple `{"error": "string"}` error bodies reused across several endpoints) by content hash, and which model name "wins" the dedup is not stable across runs — even with an unchanged spec and the same generator version. If `git diff` after regenerating shows response model classes disappearing from `graphiant_sdk/__init__.py` / `graphiant_sdk/models/__init__.py` or being renamed in `default_api.py`'s `_response_types_map`, for endpoints your spec change didn't touch:

1. Confirm it's not a real spec change: diff the specific path's `responses` block between old and new spec JSON directly.
2. If unchanged, it's generator nondeterminism — restore the class names/exports that are on `main` today rather than let them silently drop from the SDK's public API as a side effect of an unrelated spec update.

### Merge Conflicts

If you have merge conflicts:
1. Fetch latest: `git fetch origin main`
2. Rebase your branch: `git rebase origin/main`
3. Resolve conflicts and continue: `git rebase --continue`
4. Force push: `git push --force-with-lease origin your-branch`

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Type Hints (PEP 484)](https://www.python.org/dev/peps/pep-0484/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Workflows](.github/workflows/README.md)
