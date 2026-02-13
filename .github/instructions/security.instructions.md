---
applyTo: "**/*.py"
description: "Security best practices for Python development"
---

# Security Guidelines

## Input Validation
- Validate and sanitize all user inputs
- Use type hints and Pydantic models for input validation
- Never trust data from external sources without validation
- Implement proper error handling for invalid inputs

## Dependency Security
- Regularly update dependencies to latest secure versions
- Use `pip-audit` or similar tools to check for vulnerabilities
- Pin dependency versions in production environments
- Review third-party packages before adding them

## MCP Server Security
- Validate all tool parameters before processing
- Implement proper error handling to prevent information leakage
- Use secure transport protocols when applicable
- Log security-relevant events appropriately

## Data Protection
- Never log sensitive information (passwords, API keys, personal data)
- Use environment variables for sensitive configuration
- Implement proper access controls for file operations
- Sanitize outputs to prevent information disclosure

## Code Security
- Avoid using `eval()` or `exec()` with untrusted input
- Use secure random number generation for cryptographic operations
- Implement proper exception handling to avoid stack trace leakage
- Follow the principle of least privilege in code design