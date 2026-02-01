"""Daily Briefing Agent with MCP Tools."""
"""Use gmail, google calendar, yahoo news, web search and weather for daily morning update"""

import sys
import os
os.environ["BG_JOB_ISOLATED_LOOPS"] = "true"
os.environ["WATCHFILES_FORCE_POLLING"]="false"

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import InMemorySaver

from scripts import base_tools, prompts, utils

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

# model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

from langchain_openai import ChatOpenAI
model = ChatOpenAI(model='gpt-5-mini')

async def get_tools():
    mcp_config = utils.load_mcp_config("yahoo-finance", "gmail", "google-sheets")
    # mcp_config = utils.load_mcp_config()
    # print("mcp config loaded:", mcp_config)

    client = MultiServerMCPClient(mcp_config)

    mcp_tools = await client.get_tools()

    tools = mcp_tools + [base_tools.web_search, base_tools.get_weather]

    # # Filter tools that work with Gemini
    filter_tools = ['delete_email', 'batch_modify_emails', 'batch_delete_emails','delete_label','delete_filter']
    
    safe_tools = [tool for tool in tools if tool.name not in filter_tools]

    print(f"Loaded {len(safe_tools)} Tools")
    print(f"Tools Available\n{[tool.name for tool in safe_tools]}")

    return safe_tools

async def get_agent():
    tools = await get_tools()

    system_prompt = prompts.get_daily_briefing_prompt()

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt
    )

    return agent

agent = asyncio.run(get_agent())
