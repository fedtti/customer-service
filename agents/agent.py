from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

print("✅ Libraries imported.")

from .sub_agents.agent.agent import agent as agent
from .sub_agents.audit.agent import agent as audit
from .sub_agents.nba.agent import agent as nba

""" """
supervisor = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "supervisor",
    description = "Coordinate customers’ transfers to agents.",
    instruction = f"""
        You are an experienced customer service supervisor.
        Your task is to **coordinate customers’ transfers
        to agents**.

        You have specialized sub-agents:
          1. '{agent.name}' - Handles generic questions.
                              Delegate to it for ALL the customer
                              questions. Don’t do it ONLY for greetings.
          2. '{audit.name}' - Handles auditing of '{agent.name}' answers
                              to the customer.
                              Delegate to it after EACH '{agent.name}'
                              answer.
          3. '{nba.name}'   - Handles special offers for the customer.
                              Delegate to it ONLY if the customer is
                              eligible for an offer.

        For anything else, respond appropriately or state you cannot
        handle it.
    """,
    sub_agents = [
        agent,
        audit,
        nba
    ]
)

print(f"✅ Agent '{supervisor.name}' created using model '{supervisor.model.model}' with sub-agents: '{[agent.name for agent in supervisor.sub_agents]}'.")

root_agent = supervisor
