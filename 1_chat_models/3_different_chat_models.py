from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm= ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", temperature=0)
result=llm.invoke("What is the capital of France?")
print(result.content)