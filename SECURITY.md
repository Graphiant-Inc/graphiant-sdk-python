# Security Policy

## Supported Versions

We actively support the following versions with security updates:

| Version | Supported          | Notes                                    |
| ------- | ------------------ | ---------------------------------------- |
| 26.6.x  | :white_check_mark: | Current stable release (latest: **26.6.0**) |
| 26.5.x  | :white_check_mark: | Previous release line (latest: **26.5.0**) |
| 26.4.x  | :white_check_mark: | Older supported release (latest: **26.4.0**) |
| 26.3.x  | :white_check_mark: | Older supported release (latest: **26.3.3**) |
| 26.2.x  | :white_check_mark: | Older supported release  |
| 26.1.x  | :white_check_mark: | Older supported release  |
| 25.12.x | :white_check_mark: | Legacy release           |
| < 25.12 | :x:                | No longer supported      |

**Note:** We recommend always using the latest version to ensure you have the most recent security patches.

### Pygments

**Pygments** has **Regular Expression Denial of Service (ReDoS) due to Inefficient Regex for GUID Matching** in vulnerable older releases. This package declares **Pygments ≥ 2.20** as a direct dependency so installs resolve patched releases.

### Development tooling (`filelock`)

Tools such as **tox** and **virtualenv** depend on **filelock**. Older **filelock** versions were affected by a **time-of-check–time-of-use (TOCTOU)** issue in **SoftFileLock**, including a race that could allow **symlink attacks** during lock file creation. This package declares **Python ≥ 3.10** and **filelock ≥ 3.20.3** for Poetry dev dependencies so installs resolve **filelock** releases that include the relevant fixes.

### Development tooling (`pytest`)

**pytest** through **9.0.2** on UNIX used predictable **`/tmp/pytest-of-{user}`** paths in ways that allowed **local symlink / TOCTOU attacks**, leading to **denial of service** or possible **privilege escalation** (**CVE-2025-71176**, CVSS 6.8). This repository requires **pytest ≥ 9.0.3** in dev / test requirements and **Poetry** lockfile so CI and contributors resolve a patched release. Upstream references: [pytest PR #14279](https://github.com/pytest-dev/pytest/pull/14279), [CVE-2025-71176](https://www.cve.org/CVERecord?id=CVE-2025-71176).

### HTTP client (`urllib3`)

**urllib3** versions before **2.7.0** were affected by two issues relevant to clients that consume untrusted compressed responses or follow proxied low-level redirects:

- Parts of the streaming API could bypass decompression-bomb safeguards and fully decode highly compressed responses during Brotli reads or `HTTPResponse.drain_conn()`, causing excessive CPU or memory use.
- Sensitive headers such as `Authorization`, `Cookie`, and `Proxy-Authorization` could be forwarded across origins when redirects were followed through low-level proxied `urlopen(..., assert_same_host=False)` flows.

The **Poetry** lockfile is updated to **urllib3 2.7.0** for repository development and reproducible installs. The package runtime dependency range already allows **urllib3 2.7.0**; downstream applications should ensure their environment resolves **urllib3 ≥ 2.7.0** when using the SDK.

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security vulnerability, please follow these steps:

### How to Report

1. **Do NOT** open a public GitHub issue for security vulnerabilities
2. Email security details to: **security@graphiant.com**
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)
   - Your contact information

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Resolution**: Depends on severity (see below)

### Severity Levels

| Severity | Response Time | Description                                    |
|----------|---------------|------------------------------------------------|
| Critical | 24-48 hours    | Remote code execution, authentication bypass   |
| High     | 7 days         | Privilege escalation, data exposure           |
| Medium   | 30 days        | Information disclosure, denial of service     |
| Low      | 90 days        | Best practice violations, minor issues         |

### What to Expect

- **Acknowledgment**: You will receive an acknowledgment email within 48 hours
- **Updates**: Regular updates on the status of the vulnerability
- **Credit**: With your permission, we will credit you in security advisories
- **Disclosure**: We will coordinate public disclosure after a fix is available

## Security Best Practices

### Credential Management

- **Never commit secrets**: Never commit API keys, tokens, passwords, or other sensitive information to the repository
- **Use environment variables**: Store credentials in environment variables
  ```python
  import os
  
  username = os.getenv("GRAPHIANT_USERNAME")
  password = os.getenv("GRAPHIANT_PASSWORD")
  host = os.getenv("GRAPHIANT_HOST", "https://api.graphiant.com")
  ```
- **Use secure storage**: For production applications, use secure secret management systems (e.g., AWS Secrets Manager, HashiCorp Vault)
- **Rotate credentials**: Regularly rotate API keys and passwords
- **Use `.env` files carefully**: Never commit `.env` files to version control

### Code Security

- **Input Validation**: Always validate and sanitize user inputs
- **Error Handling**: Don't expose sensitive information in error messages
- **Dependency Management**: Keep dependencies up to date
  ```bash
  pip list --outdated
  pip install --upgrade package-name
  ```
- **Security Scanning**: Use tools like `bandit` for security analysis
  ```bash
  pip install bandit
  bandit -r graphiant_sdk/
  ```
- **Dependency Vulnerability Scanning**: Use `safety` to check for known vulnerabilities
  ```bash
  pip install safety
  safety check
  ```

### Dependency Management

- **Regular Updates**: Regularly update dependencies to patch security vulnerabilities
- **Vulnerability Scanning**: Use `safety` or `pip-audit` to scan for known vulnerabilities
  ```bash
  pip install pip-audit
  pip-audit
  ```
- **Minimal Dependencies**: Only include necessary dependencies in `requirements.txt`
- **Version Pinning**: Use specific versions in `requirements.txt` for production
- **Virtual Environments**: Always use virtual environments to isolate dependencies

### CI/CD Security

- **GitHub Actions Secrets**: Use GitHub Secrets for sensitive data (never hardcode)
- **Branch Protection**: All changes require review and signed commits
- **Code Scanning**: Automated security scanning in CI/CD pipelines
- **Dependency Scanning**: Automated dependency vulnerability scanning

### Repository Security

- **CODEOWNERS**: Code owners are automatically requested for review
- **Branch Protection**: Main branch is protected with required reviews
- **Signed Commits**: All commits must be verified with GPG signatures
- **Access Control**: Repository access is restricted to authorized team members

### Python-Specific Security

- **SQL Injection**: Use parameterized queries if interacting with databases
- **Code Injection**: Never use `eval()` or `exec()` with user input
- **Path Traversal**: Validate file paths and use `os.path.join()` or `pathlib`
- **Deserialization**: Be cautious with `pickle` and use safer alternatives like `json`
- **Type Safety**: Use type hints and `mypy` to catch type-related issues
- **Exception Handling**: Always handle exceptions explicitly

### Environment Variables

When using environment variables for credentials:

```python
import os
from typing import Optional

def get_credentials() -> tuple[str, str, str]:
    """
    Get credentials from environment variables.
    
    Returns:
        Tuple of (host, username, password)
        
    Raises:
        ValueError: If required credentials are missing
    """
    username = os.getenv("GRAPHIANT_USERNAME")
    if not username:
        raise ValueError("GRAPHIANT_USERNAME environment variable is required")
    
    password = os.getenv("GRAPHIANT_PASSWORD")
    if not password:
        raise ValueError("GRAPHIANT_PASSWORD environment variable is required")
    
    host = os.getenv("GRAPHIANT_HOST", "https://api.graphiant.com")
    
    return host, username, password
```

### Secure Configuration

```python
from graphiant_sdk import Configuration, ApiClient
import os

# Secure configuration using environment variables
config = Configuration(
    host=os.getenv("GRAPHIANT_HOST", "https://api.graphiant.com"),
    username=os.getenv("GRAPHIANT_USERNAME"),
    password=os.getenv("GRAPHIANT_PASSWORD")
)

# Never hardcode credentials
# BAD: config = Configuration(username="user", password="pass")
```

### Testing Security

- **Test with invalid inputs**: Test error handling and edge cases
- **Test authentication**: Verify authentication and authorization work correctly
- **Review test coverage**: Ensure security-critical paths are tested
- **Test error messages**: Ensure error messages don't leak sensitive information

### Documentation Security

- **No secrets in examples**: Never include real credentials in documentation or examples
- **Security warnings**: Document security considerations for sensitive operations
- **Best practices**: Include security best practices in documentation

## Security Checklist for Contributors

Before submitting a pull request, ensure:

- [ ] No secrets or credentials are committed
- [ ] Input validation is implemented
- [ ] Error messages don't expose sensitive information
- [ ] Dependencies are up to date
- [ ] Tests cover security-critical paths
- [ ] Code follows Python security best practices
- [ ] No hardcoded credentials or API keys
- [ ] Environment variables are used for configuration
- [ ] Security scanning tools pass (`bandit`, `safety`)

## Security Tools

### Bandit (Security Linter)

```bash
# Install
pip install bandit

# Run security scan
bandit -r graphiant_sdk/

# Generate HTML report
bandit -r graphiant_sdk/ -f html -o bandit-report.html
```

### Safety (Dependency Vulnerability Scanner)

```bash
# Install
pip install safety

# Check dependencies
safety check

# Check with requirements file
safety check -r requirements.txt
```

### pip-audit (Alternative Dependency Scanner)

```bash
# Install
pip install pip-audit

# Audit dependencies
pip-audit

# Generate requirements file
pip-audit --desc -r requirements.txt
```

## Additional Resources

- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security.html)
- [OWASP Python Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Python_Security_Cheat_Sheet.html)
- [Python Security Guide](https://python-security.readthedocs.io/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Safety Documentation](https://pyup.io/safety/)

## Contact

For security concerns, please contact: **security@graphiant.com**

---

**Last Updated**: 2026-07-08
