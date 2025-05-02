from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableMap, RunnableSequence

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
animal_fact_template = ChatPromptTemplate.from_messages([
    ("system", "You are telling facts and you say facts about {animal}."),
    ("human", "Tell me a {count} facts."),
])
translation_template = ChatPromptTemplate.from_messages([
    ("system", "You are a translator and convert provided text to {language}."),
    ("human", "Translate the following text to {language}: {text}"),
])

count_words = RunnableLambda(lambda x: f"WordCount {len(x.split())} \n {x}")
prepare_for_translation = RunnableLambda(lambda x: {"text": x, "language": "French"})

chain = animal_fact_template | llm | StrOutputParser() | prepare_for_translation | translation_template | llm | StrOutputParser() | count_words
response = chain.invoke({"animal": "cat", "count": 3})
print(response)
