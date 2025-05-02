from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableMap, RunnableSequence,RunnableParallel

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

summary_template = ChatPromptTemplate.from_messages([
    ("system", "YYou are a movie critic."),
    ("human", "Provide a shortern summary of the movie {movie_name}."),
])

def analyze_plot(plot):
    plot_template = ChatPromptTemplate.from_messages([
        ("system", "You are a movie critic."),
        ("human", "Analyze the plot :{plot}.What are the 2 strengths and weaknesses?"),
    ])
    return plot_template.format_prompt(plot=plot)

def analyze_characters(characters):
    characters_template = ChatPromptTemplate.from_messages([
        ("system", "You are a movie critic."),
        ("human", "Analyze the characters :{characters}.What are the 2 strengths and weaknesses?"),
    ])
    return characters_template.format_prompt(characters=characters)


def combine_verdicts(plot_analysis, characters_analysis):
    return f"Plot Analysis: {plot_analysis}\n\nCharacters Analysis: {characters_analysis}"

plot_branch_chain = (RunnableLambda(lambda x: analyze_plot(x)) | llm | StrOutputParser())
characters_branch_chain = (RunnableLambda(lambda x: analyze_characters(x)) | llm | StrOutputParser())

chain =( summary_template
         | llm 
         | StrOutputParser()
         | RunnableParallel(branches={"plot":plot_branch_chain,"characters":characters_branch_chain})  
         | RunnableLambda(lambda x: combine_verdicts(x["branches"]["plot"], x["branches"]["characters"]))
          
           )
response = chain.invoke({"movie_name": "Inception"})

print(response)