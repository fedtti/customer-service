from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

#
def offer() -> None:

    exit(0)

#
agent = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "nba",
    description = "Offers the Next Best Action (NBA) to the customer.",
    instruction = """
        You are an experienced customer service agent.
        Your ONLY task is to **offer the _Next Best Action (NBA)_ to the customer**.
    """
)
