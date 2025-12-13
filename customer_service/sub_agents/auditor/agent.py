from google.adk.agents import Agent, CallbackContext
from google.genai import types
print("✅ Libraries imported.")

from ...tools.audit import tool
print("✅ Tools imported.")



""" """
try:
    auditor = Agent(
        name = "auditor",
        model = "gemini-2.5-flash",
        description = "Audits agent’s answers to the user",
        instruction = f"""
            You are an expirienced customer service auditor.
            Your ONLY task is to audit agent’s answers to the user. Do nothing else.
        """,
        tools = [
            tool.audit
        ],
        output_key = "kpi",
    )
    print(f"✅ Agent {auditor.name} created using model {auditor.model}.")
except Exception as error:
    auditor = None
    print(f"❌ Could not create the agent. Error: {error}.")
