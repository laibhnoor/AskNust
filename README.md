# AI-Powered RAG Chatbot (FastAPI + LangChain) #
 
This project is a Retrieval-Augmented Generation (RAG) chatbot built with FastAPI and LangChain that allows users to query documents (PDFs, CSVs, etc.) and get context-aware answers in natural language.

It uses FAISS for vector storage, OpenAI GPT (or HuggingFace models) for LLM responses, and supports conversational memory so that follow-up questions remain contextual.

🚀 Features

✅ Document Loader – Loads multiple PDFs and CSVs from a data/ folder

✅ Chunking & Embeddings – Splits documents into manageable chunks and generates vector embeddings

✅ FAISS Vector Database – Stores document embeddings locally for fast retrieval

✅ RAG Pipeline – Retrieves most relevant chunks and passes them to an LLM for answer generation

✅ Conversational Memory – Remembers chat history for contextual follow-ups

✅ FastAPI Backend – Provides REST API endpoints for querying

✅ CORS Enabled – Works seamlessly with React (or any frontend)


##  🛠️ Tech Stack ##

Backend: FastAPI

Document Processing: LangChain + FAISS

LLM: OpenAI GPT-3.5 (configurable)

Embeddings: OpenAI Embeddings or HuggingFace Sentence Transformers

Memory: ConversationBufferMemory (LangChain)

## ⚡ Setup & Usage ##    
### 1️⃣ Clone the Repository
git clone https://github.com/laibhnoor/rag-chatbot.git
cd rag-chatbot/backend

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Configure Environment Variables
Create a .env file in the backend/ folder:
OPENAI_API_KEY=your_openai_api_key_here

### 4️⃣ Build the Vector Database
python ingest.py

This will:

Load all PDFs/CSVs from data/

Split into chunks

Create embeddings

Save FAISS index locally in vectorstore/

### 5️⃣ Run the FastAPI Server
uvicorn main:app --reload

You should see:

✅ FastAPI is running

Visit http://localhost:8000 to confirm.






