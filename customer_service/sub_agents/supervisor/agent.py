from google.adk.agents import Agent
from google.genai import types
print("✅ Libraries imported.")


""" """
try:
    supervisor = Agent(
        name = "supervisor",
        description = "Answers users’ questions",
        instruction = f"""
            You are an experienced customer service agent.
            Your ONLY task is to answer users’ question. Do nothing else.
        """,
    )
    print(f"✅ Agent {supervisor.name} created using model {supervisor.model}.")
except Exception as error:
    supervisor = None
    print(f"❌ Could not create or run the agent. Error: {error}.")
