from google.adk.agents import Agent
from google.genai import types
print("✅ Libraries imported.")



""" """
try:
    agent = Agent(
        name = "agent",
        model = "gemini-2.5-flash",
        description = "Answers users’ questions",
        instruction = f"""
            You are an experienced customer service agent.
            Your ONLY task is to answer users’ question. Do nothing else.

        """,
    )
    print(f"✅ Agent {agent.name} created using model {agent.model}.")
except Exception as error:
    agent = None
    print(f"❌ Could not create or run the agent. Error: {error}.")
