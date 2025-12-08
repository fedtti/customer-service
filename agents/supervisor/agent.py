from google.adk.agents import Agent
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
from google.genai import types

print("✅ Libraries imported.")

from .sub_agents.agent import agent as agent
from .sub_agents.audit import agent as audit

""" """
supervisor = Agent(
    model = "gemini-3-pro-preview",
    name = "supervisor",
    description = "Supervise agents’ activities",
    instruction = f"""
        You are an experienced customer service supervisor.
        Your role is to supervise agents’ activities.

        You greet the user after their first message, then:
        1.
        2.

        
    """,
    sub_agents = [
        agent,
        audit
    ],
    tools = [
      
    ]
)

print(f"✅ Agent '{supervisor.name}' created using model '{supervisor.model}' with sub-agents: {[]}, and tools: {[]}.")

root_agent = supervisor
