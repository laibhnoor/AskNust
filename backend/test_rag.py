import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DB_FAISS_PATH = "vectorstore/db_faiss"

print("🔄 Loading FAISS DB...")
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})

print("🤖 Initializing LLM...")
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# 🔍 Test a query
query = input("Ask something about your documents: ")
response = qa_chain.invoke({"query": query})
print(f"\n📢 Answer: {response['result']}")
