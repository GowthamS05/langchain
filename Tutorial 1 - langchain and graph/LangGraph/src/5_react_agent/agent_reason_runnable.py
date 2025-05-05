import datetime
from langchain_openai import ChatOpenAI
from langchain.agents import tool,create_react_agent
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
from langchain import hub

llm= ChatOpenAI(model="gpt-4o-mini", temperature=0)

search_tool = TavilySearchResults(search_depth='basic')

@tool
def get_systemTime(format:str="%Y-%m-%d %H:%M:%S"):
    """
    Get the current system time.
    Args:
        format (str): The format in which to return the time. Default is "%Y-%m-%d %H:%M:%S".
    Returns:
        str: The current system time in the specified format.
    """
    # Get the current system time
    return datetime.datetime.now().strftime(format)

tools=[search_tool,get_systemTime]

react_prompt = hub.pull("hwchase17/react")

react_agent_runnable=create_react_agent(llm=llm, tools=tools,prompt=react_prompt)


