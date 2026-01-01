from mcp.server.fastmcp import FastMCP

mcp = FastMCP("YuboDevServer")

@mcp.tool()
def get_system_status(service_name: str) -> str:
    return f"Service {service_name} is running smoothly."

if __name__ == "__main__":
    mcp.run(transport="stdio")