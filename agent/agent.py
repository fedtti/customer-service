from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from .sub_agents.audit.agent import agent as audit
from .sub_agents.nba.agent import agent as nba

agent = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "agent",
    description = "",
    instruction = """
        You are an experienced customer service agent that replies gently to the customer.
    """,
    sub_agents = [
      audit,
      nba
    ],
    tools = []
)

root_agent = agent