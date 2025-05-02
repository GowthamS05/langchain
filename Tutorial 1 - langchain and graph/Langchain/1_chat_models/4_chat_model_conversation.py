from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

model= ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
chat_history=[]
system_message=SystemMessage("You are a helpful assistant.")
chat_history.append(system_message)

while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    chat_history.append(HumanMessage(user_input))
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print(f"Assistant: {result.content}")

