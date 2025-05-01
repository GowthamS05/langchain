from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
messages = [
    ("system", "You are a helpful assistant."),
    ("human", "Write a {adjective} poem about {topic}."),
]



prompt_template = ChatPromptTemplate.from_messages(messages)
result=prompt_template.invoke({"adjective": "funny", "topic": "cats"})
llm_result = llm.invoke(result)
print(llm_result.content)
