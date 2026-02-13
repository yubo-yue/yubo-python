---
applyTo: "**/*.py"
description: "Performance optimization guidelines"
---

# Performance Guidelines

## General Performance
- Use appropriate data structures for the task (dict for lookups, set for membership tests)
- Prefer list comprehensions over loops when appropriate
- Use generator expressions for large datasets
- Cache expensive computations when possible

## Async Programming
- Use async/await for I/O-bound operations
- Avoid blocking operations in async functions
- Use asyncio.gather() for concurrent operations
- Implement proper connection pooling for external services

## MCP Server Performance
- Keep tool execution times reasonable for interactive use
- Use streaming responses for large outputs
- Implement timeout handling for long-running operations
- Cache results when appropriate and safe

## Memory Management
- Use context managers for resource cleanup
- Avoid creating unnecessary object copies
- Use __slots__ for classes with many instances
- Profile memory usage for data-intensive operations

## Optimization Strategies
- Profile before optimizing to identify bottlenecks
- Use appropriate algorithms and data structures
- Consider using NumPy for numerical computations
- Implement lazy loading for expensive resources