<!-- Based on: https://github.com/github/awesome-copilot/blob/main/instructions/python.instructions.md -->
---
applyTo: "**/*.py"
description: "Python coding conventions and guidelines"
---

# Python Coding Conventions

## Python Guidelines
- Write clear and concise comments for each function
- Ensure functions have descriptive names and include type hints
- Provide docstrings following PEP 257 conventions
- Use the `typing` module for type annotations (e.g., `List[str]`, `Dict[str, int]`)
- Break down complex functions into smaller, more manageable functions

## Code Style and Formatting
- Follow the **PEP 8** style guide for Python
- Maintain proper indentation (use 4 spaces for each level of indentation)
- Ensure lines do not exceed 79 characters
- Place function and class docstrings immediately after the `def` or `class` keyword
- Use blank lines to separate functions, classes, and code blocks where appropriate

## MCP Server Specific Guidelines
- Always include type hints - they generate schemas automatically
- Write clear docstrings - they become tool descriptions
- Use Pydantic models or TypedDicts for structured outputs
- Support async operations for I/O-bound tasks
- Include proper error handling in all MCP tools

## General Best Practices
- Always prioritize readability and clarity
- For algorithm-related code, include explanations of the approach used
- Write code with good maintainability practices, including comments on why certain design decisions were made
- Handle edge cases and write clear exception handling
- For libraries or external dependencies, mention their usage and purpose in comments
- Use consistent naming conventions and follow language-specific best practices
- Write concise, efficient, and idiomatic code that is also easily understandable