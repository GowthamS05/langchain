from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

message=[
    SystemMessage("You are a social Media Expert."),
    HumanMessage("Give me a tip to get more likes on instagram posts."),
    AIMessage("To get more likes on your Instagram posts, try using high-quality images and engaging captions. Also, consider posting at times when your audience is most active."),
    HumanMessage("What is the best time to post?"),
]
llm= ChatOpenAI(model="gpt-3.5-turbo", temperature=1)
result=llm.invoke(message)
print(result.content)