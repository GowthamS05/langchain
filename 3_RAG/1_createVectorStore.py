import os 
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "documents", "example.txt")
persistent_directory = os.path.join(current_dir,"db", "chroma_db")

if not os.path.exists(persistent_directory):
    print("Does not exist")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    loader =TextLoader(file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    docs= text_splitter.split_documents(documents)

    print("Number of documents:", len(docs))
    print("First document:", docs[0].page_content)

    print("Creating embeddings...")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )
    print("Embeddings created.")
    print("Creating Chroma vector store...")
    vector_store = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=persistent_directory
    )
    print("Chroma vector store created.")

else:
    print("Chroma vector store already exists.")
    
