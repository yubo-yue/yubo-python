---
applyTo: "**/test_*.py,**/*_test.py,**/tests/**/*.py"
description: "Testing standards and practices for Python projects"
---

# Testing Guidelines

## Testing Framework
- Use `pytest` for unit testing and test discovery
- Use `pytest-asyncio` for testing async functions
- Use `unittest.mock` for mocking external dependencies

## Test Structure
- Follow the Arrange-Act-Assert pattern in test functions
- Use descriptive test function names that explain what is being tested
- Group related tests in test classes when appropriate
- Use fixtures for common test setup and teardown

## MCP Tool Testing
- Test MCP tools independently before LLM integration
- Mock external API calls and I/O operations
- Test both successful and error conditions
- Verify type safety and schema generation

## Coverage and Quality
- Always include test cases for critical paths of the application
- Account for common edge cases like empty inputs, invalid data types, and large datasets
- Include comments for edge cases and the expected behavior in those cases
- Aim for high test coverage but focus on meaningful tests

## Test Organization
- Mirror the source code structure in test directories
- Use `conftest.py` for shared fixtures and configuration
- Keep test files focused and avoid overly complex test logic
- Document complex test scenarios with docstrings