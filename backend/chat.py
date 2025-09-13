# chat.py
from fastapi import APIRouter
from pydantic import BaseModel
from rag_pipeline import retriever, llm  # ✅ Import retriever + llm from rag_pipeline
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

router = APIRouter()

# ✅ Create memory (persists as long as FastAPI server is running)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ✅ ConversationalRetrievalChain remembers past interactions
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
async def chat(request: ChatRequest):
    # ✅ Include memory so conversation stays contextual
    result = await qa_chain.acall({"question": request.query})
    return {"answer": result["answer"]}
