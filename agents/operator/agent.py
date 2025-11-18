from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from .sub_agents.nba import nba

root_agent = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "operator",
    description = "",
    instruction = """
        You are a good agent.
    """,
    sub_agents = [
      nba
    ]
)
