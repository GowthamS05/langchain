from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
from pymongo import MongoClient
from langgraph.checkpoint.mongodb import MongoDBSaver



load_dotenv()

# sqlLite_conn = sqlite3.connect("checkpoint.sqlite",check_same_thread=False)
mongodb_client = MongoClient("mongodb+srv://langchain:<password>@langchaincluster.thakg1e.mongodb.net/")


# memory = SqliteSaver(sqlLite_conn)
memory = MongoDBSaver(mongodb_client)


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

config={"configurable":{"thread_id":1545}}

while True: 
    user_input = input("User: ")
    if(user_input in ["exit", "end"]):
        break
    else: 
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        }, config=config)

        print("AI: " + result["messages"][-1].content)