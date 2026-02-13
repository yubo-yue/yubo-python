---
agent: 'agent'  
model: Claude Sonnet 4
tools: ['codebase']
description: 'Generate comprehensive tests for Python code'
---

# Write Python Tests

Generate comprehensive test cases for Python functions and classes following the testing guidelines in [testing.instructions.md](../instructions/testing.instructions.md).

## Test Requirements
- Use `pytest` framework with appropriate fixtures
- Follow Arrange-Act-Assert pattern
- Test both successful and error conditions
- Include edge cases and boundary conditions
- Mock external dependencies and I/O operations

## Test Structure Template
```python
import pytest
from unittest.mock import Mock, patch

class TestClassName:
    def test_successful_case(self):
        # Arrange
        # Act  
        # Assert
        pass
    
    def test_error_condition(self):
        # Arrange
        # Act & Assert (for exceptions)
        with pytest.raises(SpecificException):
            # code that should raise exception
            pass
    
    def test_edge_case(self):
        # Test boundary conditions
        pass
```

## MCP Tool Testing
For MCP tools, ensure tests cover:
- Type hint validation and schema generation
- Tool description accuracy
- Parameter validation
- Return value structure
- Error handling behavior
- Async operation correctness

## Coverage Guidelines
- Test all public methods and functions
- Cover error paths and exception handling
- Test with various input types and sizes
- Verify type safety and schema compliance
- Mock external services and file operations

Ask for the code to test if not provided, then generate complete test cases with appropriate fixtures and assertions.