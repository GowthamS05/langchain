from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

positive_feedback_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Generate a thank you not for positive feedback {feedback}."),
])

negative_feedback_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Generate a '' response addressing this negative feedback {feedback}."),
])

neutral_feedback_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Generate a request more details for this neutral feedback {feedback}."),
])

esclate_feedback_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Generate a response to escalated this feedback to human agent {feedback}."),
])

clasification_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Classify the feedback {feedback} as positive, negative, neutral or escalated."),
])

branches = RunnableBranch(
    (
        lambda x: "positive" in x,
        positive_feedback_template | llm | StrOutputParser()
    ),
    (
        lambda x: "negative" in x,
        negative_feedback_template | llm | StrOutputParser()
    ),
    (
        lambda x: "neutral" in x,
        neutral_feedback_template | llm | StrOutputParser()
    ),
    esclate_feedback_template | llm | StrOutputParser()

)

clasification_chain=clasification_template | llm | StrOutputParser()

chain = clasification_chain | branches

response=chain.invoke({"feedback": "The product is great, but the delivery was late."})
print(response)
