---
agent: 'agent'
model: Claude Sonnet 4
tools: ['codebase']
description: 'Refactor and improve existing Python code'
---

# Python Code Refactoring

Refactor existing Python code to improve quality, performance, and maintainability while following the guidelines in [python.instructions.md](../instructions/python.instructions.md).

## Refactoring Objectives
1. **Code Quality**: Improve readability, maintainability, and structure
2. **Performance**: Optimize for better execution speed and memory usage
3. **Standards Compliance**: Ensure PEP 8 compliance and best practices
4. **Type Safety**: Add or improve type hints throughout
5. **Documentation**: Enhance docstrings and comments

## Refactoring Checklist

### Structure & Design
- [ ] Break large functions into smaller, focused functions
- [ ] Remove code duplication through extraction
- [ ] Improve class design and inheritance structure
- [ ] Apply appropriate design patterns

### Code Quality
- [ ] Add comprehensive type hints
- [ ] Improve variable and function naming
- [ ] Enhance error handling with specific exceptions
- [ ] Add or improve docstrings

### Performance
- [ ] Optimize data structures and algorithms
- [ ] Implement caching where appropriate
- [ ] Use async/await for I/O operations
- [ ] Reduce memory allocations and copies

### MCP Server Specific
- [ ] Ensure type hints generate proper schemas
- [ ] Optimize tool execution time
- [ ] Improve error messages for better UX
- [ ] Add proper logging and monitoring

## Refactoring Process
1. **Analyze**: Identify specific issues and improvement opportunities
2. **Plan**: Outline the refactoring strategy and steps
3. **Implement**: Make changes incrementally with testing
4. **Validate**: Ensure functionality is preserved
5. **Document**: Update documentation to reflect changes

## Safety Guidelines
- Preserve existing functionality and behavior
- Maintain backward compatibility where possible
- Add tests before refactoring complex logic
- Use version control to track changes safely

Provide the code to refactor, and I'll create an improved version with detailed explanations of the changes made.