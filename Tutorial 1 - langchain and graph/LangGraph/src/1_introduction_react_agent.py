import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType,tool
from langchain_community.tools import TavilySearchResults

load_dotenv()
 
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

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

agent=  initialize_agent(tools=tools,llm=llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

result =agent.invoke("Give me a today whether report of chennai? and also tell me the current time in chennai")

print(result)


