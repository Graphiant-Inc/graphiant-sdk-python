# GitHub Actions Workflows

This directory contains GitHub Actions workflows for the Graphiant SDK Python package.

## Workflows

### `lint.yml` - Code Quality Checks
Comprehensive linting workflow that runs multiple code quality checks in parallel:
- **Flake8** - Python style guide (PEP 8) and code quality checks
- **MyPy** - Static type checking

### `test.yml` - Testing
Runs all tests for the SDK:
- **`test` job** - Matrix job testing against Python 3.11, 3.12, 3.13:
  - Unit tests with pytest
  - Code coverage reporting
  - Coverage reports uploaded to Codecov (Python 3.12 only)

### `build.yml` - Build Package
Builds the Python package:
- Creates wheel and source distribution
- Verifies build artifacts were created successfully
- Uploads build artifacts

### `release.yml` - Release and Publish
Publishes the package to PyPI and creates GitHub releases:
- Manual trigger only (workflow_dispatch)
- Restricted to repository admins and maintainers only
- Requires `PYPI_API_TOKEN` secret to be set for publishing
- Optional: Can build without publishing (for testing)
- Optional: Creates Git tag and GitHub release after successful PyPI publish

## Setup

### Required Secrets

#### For Release Workflow

For the release workflow to publish to PyPI, you need to set up the following secret in GitHub:

1. **Create a PyPI API Token:**
   - Go to https://pypi.org/manage/account/token/
   - Click "Add API token"
   - **Important**: Select "Entire account" or create a project-scoped token for this specific package
   - Give it a descriptive name (e.g., "graphiant-sdk-python GitHub Actions")
   - Copy the token immediately (you won't be able to see it again)
   - **Note**: The token should be 40+ characters long

2. **Add the token to GitHub:**
   - Go to your repository settings
   - Navigate to **Secrets and variables** → **Actions**
   - Click "New repository secret"
   - **Name**: `PYPI_API_TOKEN`
   - **Value**: Paste the PyPI API token (ensure no extra whitespace)
   - Click "Add secret"

3. **Verify token setup:**
   - Ensure the token has "Upload packages" permission
   - For project-scoped tokens, ensure it's scoped to the correct package name
   - Check that there's no leading/trailing whitespace in the secret value

**Troubleshooting 403 Forbidden errors:**
- Token is invalid or expired → Generate a new token
- Token doesn't have upload permissions → Check token scope at https://pypi.org/manage/account/token/
- Token is for TestPyPI → Use a production PyPI token
- Package version already exists → PyPI doesn't allow overwriting; increment version
- Token has whitespace → Re-add the secret without extra spaces

#### Optional Secrets/Variables for Test Workflow

The test workflow can optionally use Graphiant API credentials to run integration tests (e.g., `test_sanity.py`). If these are not configured, credential-dependent tests will be skipped.

To enable integration tests:

1. Go to your repository settings
2. Navigate to **Secrets and variables** → **Actions**
3. Add the following secrets or variables:
   - **Name**: `GRAPHIANT_HOST`
     - **Value**: Your Graphiant API host (e.g., `https://api.graphiant.com`)
     - **Note**: Can be configured as either a secret or a variable
   - **Name**: `GRAPHIANT_USERNAME`
     - **Value**: Your Graphiant API username
     - **Note**: Should be configured as a secret for security
   - **Name**: `GRAPHIANT_PASSWORD`
     - **Value**: Your Graphiant API password
     - **Note**: Must be configured as a secret for security

The workflow will check for these credentials and run integration tests if they are available. If not configured, the workflow will still run but skip credential-dependent tests.

### Workflow Triggers

- **Pull Requests**: All workflows run on PRs to ensure code quality
- **Push to main/develop**: CI workflows run on pushes to main branches
- **Scheduled**: Test workflow runs nightly at 2 AM UTC
- **Manual**: Release workflow must be manually triggered via workflow_dispatch (restricted to admins and maintainers)

## Usage

### Running Workflows Locally

While you can't run GitHub Actions locally, you can run the same commands:

```bash
# Linting
pip install -r requirements.txt
pip install -r test-requirements.txt
flake8 graphiant_sdk/ --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 graphiant_sdk/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
mypy graphiant_sdk/

# Testing
# Without credentials (credential-dependent tests will be skipped)
pytest --cov=graphiant_sdk --cov-report=xml --cov-report=term

# With credentials (for integration tests)
export GRAPHIANT_HOST="https://api.graphiant.com"
export GRAPHIANT_USERNAME="your-username"
export GRAPHIANT_PASSWORD="your-password"
pytest --cov=graphiant_sdk --cov-report=xml --cov-report=term

# Building
pip install build wheel
python -m build

# Publishing (requires PyPI credentials)
pip install twine
twine check dist/*
twine upload dist/*
```

### Publishing a Release

1. Ensure the version in `setup.py` and `pyproject.toml` matches the version you want to publish
2. Manually trigger the release workflow via `workflow_dispatch` from the GitHub Actions tab
3. Provide the package version when prompted (should match setup.py/pyproject.toml)
   - Version can be provided with or without 'v' prefix (e.g., `25.12.1` or `v25.12.1`)
   - The workflow will normalize it to include 'v' prefix for the Git tag
4. Choose whether to publish to PyPI (default: false, for testing builds)
5. Choose whether to create Git tag and GitHub release (default: true)
   - Only creates tag/release if publishing to PyPI is enabled
6. The workflow will:
   - Build the package
   - Optionally publish to PyPI (if enabled)
   - Optionally create Git tag and GitHub release (if both publish and create_tag are enabled)

## Workflow Status

You can view workflow status in the **Actions** tab of your GitHub repository.
