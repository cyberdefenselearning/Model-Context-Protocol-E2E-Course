from mcp.server.fastmcp import FastMCP
mcp = FastMCP("hello-world")

@mcp.tool()
async def hello_world() -> str:
    """
        Hello World from MCP
    """
    return f"Hello World from MCP!"

# Assignment Say Hello
@mcp.tool()
async def greetings(name:str) -> str:
    """Greetings to a person.
    Args:
        name (str): The name of the person to greet.
        """
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport='stdio')
