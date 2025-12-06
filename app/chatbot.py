from langchain_ollama import ChatOllama  # type: ignore
from langchain_community.vectorstores import FAISS  # type: ignore
from langchain_core.messages import HumanMessage
from rag import load_vector_store  # type: ignore

# Load vectorstore once
vs = load_vector_store()

# Connect to Ollama running on RunPod
llm = ChatOllama(
    base_url="http://69.30.85.69:22112",  # Your RunPod Ollama IP and port
    model="llama3"
)

def ask_rowan_bot(query: str):
    # STEP 1 — Retrieve relevant documents
    docs = vs.similarity_search(query, k=4)
    context = "\n\n".join([d.page_content for d in docs])

    # STEP 2 — Create prompt
    prompt = f"""
You are Rowan University's information assistant.

Context from Rowan official data:
{context}

Answer the following question clearly using ONLY the above data:

Question: {query}
"""

    # STEP 3 — Send prompt to LLM
    response = llm.invoke(prompt)

    # STEP 4 — Return the model's response
    return response.content


