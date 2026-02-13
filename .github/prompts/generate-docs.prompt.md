---
agent: 'agent'
model: Claude Sonnet 4
tools: ['codebase']  
description: 'Generate comprehensive documentation'
---

# Documentation Generator

Generate comprehensive documentation for Python code following the standards in [documentation.instructions.md](../instructions/documentation.instructions.md).

## Documentation Types

### API Documentation
- Function and class reference documentation
- Parameter descriptions with types and examples
- Return value documentation
- Exception documentation with conditions
- Usage examples with code snippets

### MCP Server Documentation
- Tool descriptions and usage examples
- Server configuration and setup instructions
- Transport mode explanations
- Integration guides for Claude Desktop
- Troubleshooting and FAQ sections

### Project Documentation
- README files with clear setup instructions
- Architecture and design documentation
- Development workflow and contribution guides
- Deployment and configuration guides

## Documentation Format

### Docstring Template
```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Brief description of the function.
    
    Longer description providing more context and details
    about the function's behavior and use cases.
    
    Args:
        param1 (type): Description of parameter including
                      valid values and constraints.
        param2 (type): Description of parameter.
    
    Returns:
        return_type: Description of return value including
                    structure and possible values.
    
    Raises:
        ValueError: When input validation fails.
        RuntimeError: When operation cannot complete.
    
    Example:
        >>> result = function_name("value1", 42)
        >>> print(result)
        Expected output
    """
```

### Markdown Structure
- Use clear hierarchical headings
- Include table of contents for long documents
- Add code examples with syntax highlighting
- Include links between related sections
- Provide practical examples and use cases

## Content Guidelines
- Write for the intended audience (developers, users, contributors)
- Include both reference information and tutorials
- Provide troubleshooting information
- Keep examples current and tested
- Use consistent terminology throughout

Provide the code or project area to document, and I'll generate comprehensive documentation.