from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

#
agent = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "agent",
    description = "Answer customers’ questions.",
    instruction = """
        You are an experienced customer service agent.
        Your role is to **answer customers’ questions**.
    """
)
