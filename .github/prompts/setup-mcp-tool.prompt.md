---
agent: 'agent'
model: Claude Sonnet 4
tools: ['codebase']
description: 'Generate a new MCP tool component'
---

# Generate MCP Tool

Create a new MCP (Model Context Protocol) tool for the FastMCP server with the following requirements:

## Tool Requirements
- Include proper type hints for automatic schema generation
- Write clear docstrings that become tool descriptions
- Implement comprehensive error handling
- Support async operations for I/O-bound tasks
- Follow Python coding conventions from [python.instructions.md](../instructions/python.instructions.md)

## Tool Template Structure
```python
@mcp.tool()
def tool_name(param1: type, param2: type) -> ReturnType:
    """
    Clear description of what this tool does.
    
    Args:
        param1 (type): Description of parameter
        param2 (type): Description of parameter
    
    Returns:
        ReturnType: Description of return value
    
    Raises:
        ValueError: When invalid input is provided
        RuntimeError: When operation fails
    """
    # Implementation here
    pass
```

## Implementation Guidelines
1. **Validation**: Validate all inputs before processing
2. **Error Handling**: Use try-catch blocks with specific exception types
3. **Documentation**: Include usage examples in docstring
4. **Testing**: Consider how the tool will be tested independently
5. **Performance**: Keep execution time reasonable for interactive use

## Output Requirements
- Return structured data when possible (use TypedDict or Pydantic)
- Provide meaningful error messages
- Log important operations to stderr
- Handle edge cases gracefully

Ask for the tool name and functionality if not provided, then generate the complete tool implementation.