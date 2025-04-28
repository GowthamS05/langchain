import os 
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "documents", "example.txt")
persistent_directory = os.path.join(current_dir,"db", "chroma_db")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
)
db= Chroma(
    embedding_function=embeddings,
    persist_directory=persistent_directory
)

query="Where is Effiel tower?"

retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3,"score_threshold": 0.2}
    )
relevant_docs = retriever.invoke(query)

print("Relevant documents:")
for i, doc in enumerate(relevant_docs,1):
    print(f"Document {i}: \n {doc.page_content}\n")
    if doc.metadata:
        print(f"Metadata: {doc.metadata.get('source','Unknown')}\n")