from google.adk.agents import Agent
from google.genai import types
print("✅ Libraries imported.")


from .sub_agents.agent import agent
from .sub_agents.auditor import auditor
from .sub_agents.supervisor import supervisor
print("✅ Agents imported.")


""" """
try:
    administrator = Agent(
        name = "administrator",
        model = "gemini-2.5-flash",
        description = "Administrate agents’ operations",
        instruction = f"""
            You are an experienced customer service administrator.
            Your role is to administrate agents’ operations. You DO NOT respond to the user queries directly.

            You have three specialized sub-agents:
            1. '{agent.name}': Handles users’ queries. Delegate to it for EACH query sent by the user, UNLESS it got negative feedbacks.
            2. '{auditor.name}': Audits agent’s answers. Delegate to it EVERY time '{agent.name}' responds to the user for auditing.
            3. '{supervisor.name}': Supervises agents’ operations. Delegate to it ONLY if agent’s responses got negative feedbacks.
        """,
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


root_agent = administrator
