from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatGroq(model="llama-3.1-8b-instant")

GENERATE_POST ="generate_post"
GET_REVIEW_DECISION = "get_review_decision"
POST = "post"
COLLECT_FEEDBACK = "collect_feedback"

def generate_post(state: State):
    """Generate a post based on the user's input."""
    return {
        "messages": [llm.invoke(state["messages"])]
    }

def get_review_decision(state: State):
    """Get the review decision from the user."""
    post_content = state["messages"][-1].content
    print(f"Generated Post: {post_content}")
    decision = input("Do you want to post this? (yes/no): ")
    if decision.lower() == "yes":
        return POST
    else:
        return COLLECT_FEEDBACK
    
def post(state: State):
    """Post the content."""
    post_content = state["messages"][-1].content
    print(f"Posting: {post_content}")

def collect_feedback(state: State):
    feedback= input("Please provide your feedback: ")
    print(f"Feedback received: {feedback}")
    return {
        "messages": [HumanMessage(content=feedback)]
    }

graph = StateGraph(State)

graph.add_node(GENERATE_POST, generate_post)
graph.add_node(GET_REVIEW_DECISION, get_review_decision)
graph.add_node(COLLECT_FEEDBACK, collect_feedback)
graph.add_node(POST, post)

graph.set_entry_point(GENERATE_POST)
graph.add_conditional_edges(GENERATE_POST, get_review_decision)
graph.add_edge(POST, END)
graph.add_edge(COLLECT_FEEDBACK, GENERATE_POST)

app = graph.compile()

response = app.invoke({
    "messages": [HumanMessage(content="Generate a post about the benefits of AI in healthcare in 25 words.")]
})

print("response",response)