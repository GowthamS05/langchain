
**What is a MessageGraph?**

It is a class that LangGraph provides that we can use to orchestrate the flow of messages between different nodes.

Example use cases include:
* Simple routing decisions
* Simple chatbot conversation flow

If you just want to pass messages along between nodes, then go for MessageGraph.

If the app requires complex state management, you would use StateGraph instead (with more information on StateGraph to follow).

MessageGraph maintains a list of messages and decides the flow of those messages between nodes.

Here's how it works:
* Every node in MessageGraph receives the full list of previous messages as input.
* Each node can append new messages to the list and return it.
* The updated message list is then passed to the next node.

This mechanism allows MessageGraph to orchestrate the flow of conversation or messages through a defined sequence of nodes.

