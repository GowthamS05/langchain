from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

generate_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Twitter techie assistant tasked with writing excellent tweets."
         "Generate a best twitter post possible for user query."
         "If user provides the critic , respond with the revised version of your previous attempts"
         ),
         MessagesPlaceholder(variable_name="messages"),
    ]
)

reflect_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Viral twitter influencer grading a tweet. Generate critique and "
        "recommendation for improvement."
         "Always provide a detailed recommendation , including request for length,virality ,style etc"
         ),
         MessagesPlaceholder(variable_name="messages"),
    ]
)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

generation_chain = generate_prompt | llm

reflection_chain = reflect_prompt | llm