from google.adk.agents import Agent
from google.genai import types
print("✅ Libraries imported.")


""" """
try:
    auditor = Agent(
        name = "auditor",
        model = "gemini-2.5-flash",
        description = "Audits agent’s answers to the user",
        instruction = f"""
            You are an expirienced customer service auditor.
            Your ONLY task is to audit agent’s answers to the user. Do nothing else.

            Return a vote from 1 to 5 to the answer.
        """,
        output_key = "kpi"
    )
    print(f"✅ Agent {auditor.name} created using model {auditor.model}.")
except Exception as error:
    auditor = None
    print(f"❌ Could not create or run the agent. Error: {error}.")
