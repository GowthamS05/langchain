from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

memory = MemorySaver()

llm = ChatGroq(model="llama-3.1-8b-instant")    

class BasicChatState(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: BasicChatState):
    """Chatbot function to process messages."""
    return {
        "messages": [llm.invoke(state["messages"])]
    }

graph = StateGraph(BasicChatState)
graph.add_node("chatbot", chatbot)
graph.set_entry_point("chatbot")
graph.add_edge("chatbot", END)

app = graph.compile(checkpointer=memory)

config={"configurable":{"thread_id":1}}

response1=app.invoke({
        "messages":  HumanMessage(content="Hi , i am gowtham")
    },config=config)

response2=app.invoke({
        "messages": HumanMessage(content="What is my name?"),
    },config=config)
print("\n")

print(response1)
print("\n")
print(response2)