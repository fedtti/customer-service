from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

agent = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "nba",
    description = "",
    instruction = """
        You are an experienced customer service agent that offers the next best action to the customer.
    """,
    tools = []
)
