# backend/ingest.py
"""
import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# Path to your data folder
DATA_PATH = "../data"
DB_FAISS_PATH = "vectorstore/db_faiss"

def load_documents():
    docs = []

    # Load all PDFs
    pdf_loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    docs.extend(pdf_loader.load())

    # Load all CSVs
    csv_loader = DirectoryLoader(DATA_PATH, glob="*.csv", loader_cls=CSVLoader)
    docs.extend(csv_loader.load())

    return docs

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # number of characters per chunk
        chunk_overlap=100  # overlap between chunks
    )
    return text_splitter.split_documents(documents)

def create_vector_db():
    print("📂 Loading documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")

    print("✂️ Splitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    print("🧠 Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("💾 Saving FAISS index...")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_FAISS_PATH)
    print(f"✅ Vector DB saved at {DB_FAISS_PATH}")

if __name__ == "__main__":
    create_vector_db()

"""
from langchain.embeddings.openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DATA_PATH = "../data"
DB_FAISS_PATH = "vectorstore/db_faiss"

def load_documents():
    docs = []
    pdf_loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    docs.extend(pdf_loader.load())
    csv_loader = DirectoryLoader(DATA_PATH, glob="*.csv", loader_cls=CSVLoader)
    docs.extend(csv_loader.load())
    return docs

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    return text_splitter.split_documents(documents)

def create_vector_db():
    print("📂 Loading documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")

    print("✂️ Splitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    print("🧠 Creating OpenAI embeddings...")
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    print("💾 Saving FAISS index...")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_FAISS_PATH)
    print(f"✅ Vector DB saved at {DB_FAISS_PATH}")

if __name__ == "__main__":
    create_vector_db()

