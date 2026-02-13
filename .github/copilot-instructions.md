# GitHub Copilot Instructions for YuboDevServer Python Project

This is a Python project focused on MCP (Model Context Protocol) server development and AI/ML experimentation.

## Project Overview
- **Primary Language**: Python 3.11+
- **Project Type**: MCP Server Development & AI/ML Experimentation  
- **Key Technologies**: FastMCP, LangChain, Conda environment management
- **Development Style**: Educational with production-ready code standards

## Global Standards
- Follow all language-specific instructions in `.github/instructions/`
- Prioritize code clarity and educational value
- Include comprehensive type hints and documentation
- Use async/await for I/O-bound operations
- Implement proper error handling and validation

## Project-Specific Guidelines
- MCP tools should include clear docstrings that become tool descriptions
- All functions must have type hints for automatic schema generation
- Use Pydantic models for structured outputs when applicable
- Test MCP tools independently before integration
- Log to stderr to avoid stdout pollution in MCP servers

## Development Workflow
1. Use conda environments for dependency management
2. Test MCP servers with `uv run mcp dev server.py`
3. Install to Claude Desktop with `uv run mcp install server.py`
4. Write unit tests for all MCP tools
5. Document tool usage and examples

## File Organization
- `server.py` - Main MCP server implementation
- `*.ipynb` - Jupyter notebooks for experimentation
- `environment.yml` - Conda environment specification
- `tests/` - Unit tests for MCP tools