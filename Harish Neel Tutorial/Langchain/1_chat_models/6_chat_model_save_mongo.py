from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# MongoDB connection string (could come from your .env)
MONGODB_CONNECTION_STRING = "mongodb+srv://langchain:<password>@langchaincluster.thakg1e.mongodb.net/"

DB_NAME = "chat_db1"
COLLECTION_NAME = "chat_data2"
SESSION_ID = "user_session_1"

print("Initializing MongoDB client...")
client = MongoClient(MONGODB_CONNECTION_STRING)

print("Initializing MongoDBChatMessageHistory...")
message_history = MongoDBChatMessageHistory(
    connection_string=MONGODB_CONNECTION_STRING,
    database_name=DB_NAME,
    collection_name=COLLECTION_NAME,
    session_id=SESSION_ID,
)

print("MongoDBChatMessageHistory initialized.")
print("Current chat history:")

for message in message_history.messages:
    print(f"{message.content}")

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
system_message = SystemMessage("You are a helpful assistant.")
message_history.add_message(system_message)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    message_history.add_user_message(HumanMessage(user_input))
    result = model.invoke(message_history.messages)
    message_history.add_ai_message(AIMessage(result.content))
    print(f"Assistant: {result.content}")
