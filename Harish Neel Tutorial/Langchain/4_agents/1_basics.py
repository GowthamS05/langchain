from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain import hub
import datetime
from langchain.agents import create_react_agent, AgentExecutor,tool

load_dotenv()

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
    

llm= ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt_template =  hub.pull("hwchase17/react")


tools =[get_systemTime]

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query="What is the  current time? Show me current time not date"

llm_result = agent_executor.invoke({"input": query})

print(llm_result)

