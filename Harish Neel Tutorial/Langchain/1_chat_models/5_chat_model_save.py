from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

PROJECT_ID = "lanchain-605a3"  
COLLECTION_NAME = "chat_history" 
SESSION_ID = "user_session_1"

print("Initializing Firestore client...")

client= firestore.Client(project=PROJECT_ID)
print("Initializing FirestoreChatMessageHistory...")
message_history= FirestoreChatMessageHistory(
    client=client,
    collection=COLLECTION_NAME,
    session_id=SESSION_ID
)
print("FirestoreChatMessageHistory initialized.")
print("Current chat history:")

for message in message_history.messages:
    print(f"{message.content}")


model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
system_message=SystemMessage("You are a helpful assistant.")
message_history.add_message(system_message)

while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    message_history.add_user_message(HumanMessage(user_input))
    result=model.invoke(message_history.messages)
    message_history.add_ai_message(AIMessage(result.content))
    print(f"Assistant: {result.content}")

