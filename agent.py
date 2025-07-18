
from llm import get_llm
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from tools.python_repl import python_tool
from tools.outlook_tools import tools as outlook_tools

llm = get_llm()
tools = [python_tool] + outlook_tools

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(query: str) -> str:
    return agent.run(query)
