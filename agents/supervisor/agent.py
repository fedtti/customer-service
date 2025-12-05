from google.adk.agents.llm_agent import Agent
from google.genai import types

print("✅ Libraries imported.")

""" """
supervisor = Agent(
    model = "gemini-3-pro-preview",
    name = "supervisor",
    description = "Supervise agents",
    instruction = f"""
        You are an experienced customer service supervisor.
        Your role is to supervise agents activities’.
    """,
    sub_agents = [
      
    ],
    tools = [
      
    ]
)

print(f"✅ Agent '{supervisor.name}' created using model '{supervisor.model}' with sub-agents: {[]}, and tools: {[]}.")

root_agent = supervisor
