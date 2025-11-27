from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

from .sub_agents.agent.agent import agent as agent
from .sub_agents.audit.agent import agent as audit
from .sub_agents.nba.agent import agent as nba

#
supervisor = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "supervisor",
    description = "Coordinate customers’ transfers to agents.",
    instruction = """
        You are an experienced customer service supervisor.
        Your role is to **coordinate customers’ transfers to agents**.

        Respond with a polite greeting to the customer’s first question,
        then say: 'You are being transferred to an agent…' and transfer
        it to the sub-agent called 'agent'.
    """,
    sub_agents = [
        agent,
        audit,
        nba
    ]
)

root_agent = supervisor
