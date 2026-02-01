"""Airbnb MCP Server."""

import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")


async def get_tools():
    client = MultiServerMCPClient(
        {
            "airbnb": {
                "command": "npx",
                "args": ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
                "transport": "stdio",
            }
        }
    )

    mcp_tools = await client.get_tools()

    tools = mcp_tools

    print(f"Loaded {len(tools)} Tools")
    # print(f"Tools Available\n{tools}")

    return tools

async def main():
    tools = await get_tools()
    print(f"Tools: {tools}")

    agent = create_agent(model=model, tools=tools)
    return agent

agent = asyncio.run(main())
