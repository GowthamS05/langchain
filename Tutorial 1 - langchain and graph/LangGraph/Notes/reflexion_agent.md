## Reflexion Agent System:

The reflexion agent, similar to reflection agent, not only critiques it's own responses but also fact checks it with external data by making API calls (Internet Search)

In the Reflection agent pattern, we had to rely on the training data of LLMs but in this case, we're not limited to that.

The main component of Reflexion Agent System is the "actor"

The "actor" is the main agent that drives everything - it reflects on it's responses and re-executes.

It can do this with or without tools to improve based on self-critique that is grounded in external data

It's main sub-components include:
1. Tools/tool execution
2. Initial responder: generate an initial response & self-reflection
3. Revisor: re-respond & reflect based on previous reflections