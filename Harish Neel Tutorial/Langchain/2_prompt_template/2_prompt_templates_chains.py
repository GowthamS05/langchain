from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
messages = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Write a {adjective} poem about {topic}."),
])

chain = messages | llm | StrOutputParser()

llm_result = chain.invoke({"adjective": "funny", "topic": "cats"})
print(llm_result)
