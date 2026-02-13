---
applyTo: "**/*.py"
description: "Code review standards and GitHub review guidelines"
---

# Code Review Guidelines

## Review Checklist
- Verify all functions have proper type hints and docstrings
- Check for proper error handling and edge case coverage
- Ensure code follows PEP 8 style guidelines
- Verify test coverage for new functionality

## MCP Server Review Focus
- Validate that tool descriptions are clear and helpful
- Check that type hints generate correct schemas
- Verify proper async/await usage for I/O operations
- Ensure error handling doesn't leak sensitive information

## Security Review Points
- Check for proper input validation and sanitization
- Verify no sensitive data is logged or exposed
- Review dependency updates for security implications
- Ensure proper access controls are implemented

## Performance Review
- Look for potential performance bottlenecks
- Check for proper resource cleanup
- Verify efficient use of data structures and algorithms
- Review async operations for proper concurrency

## Documentation Review
- Ensure all public APIs are documented
- Check that examples are accurate and helpful
- verify docstrings match actual function behavior
- Review README and setup instructions for clarity