from typing import List, Sequence
from langchain_core.messages import BaseMessage, HumanMessage,ToolMessage
from langgraph.graph import END, MessageGraph
from chains import first_responsder_chain, revisor_chain
from execute_tools import execute_tools


graph = MessageGraph()
MAX_ITERATIONS=2


graph.add_node("draft", first_responsder_chain)
graph.add_node("execute_tools", execute_tools)
graph.add_node("revise", revisor_chain)

graph.add_edge("draft", "execute_tools")
graph.add_edge("execute_tools", "revise")

def event_loop(state: List[BaseMessage]) -> str:
    count_tool_visits = sum(isinstance(item, ToolMessage) for item in state)
    num_iterations = count_tool_visits
    if num_iterations > MAX_ITERATIONS:
        return END
    return "execute_tools"

graph.add_conditional_edges("revise", event_loop)
graph.set_entry_point("draft")

app=graph.compile()

print(app.get_graph().draw_mermaid())

response = app.invoke(HumanMessage(content="Write about how small business can leverage AI to grow"))
print(response[-1].tool_calls[0]['args']['answer'])




