from google.adk.agents import Agent
from google.genai import types
print("✅ Libraries imported.")

from .sub_agents.agent import agent
from .sub_agents.auditor import auditor
from .sub_agents.supervisor import supervisor
print("✅ Agents imported.")

from .prompt import INSTRUCTION
print("✅ Instructions imported.")



""" """
try:
    administrator = Agent(
        name = "administrator",
        model = "gemini-2.5-flash",
        description = "Administrate agents’ operations",
        instruction = INSTRUCTION,
        sub_agents = [
            agent,
            auditor,
            supervisor,
        ],
    )
    print(f"✅ Agent {administrator.name} created using model {administrator.model}.") # TODO: @fedtti
except Exception as error:
    administrator = None
    print(f"❌ Could not create or run the agent. Error: {error}.")



root_agent = administrator # Export for Agent Development Kit (ADK).
