from langchain_ollama import ChatOllama # type: ignore
from langchain_community.vectorstores import FAISS # type: ignore
from langchain_core.messages import HumanMessage
from app.rag import load_vector_store # type: ignore

# Load vectorstore once
vs = load_vector_store()

# Use a stable LLM model
llm = ChatOllama(model="mistral", temperature=0.2)

def ask_rowan_bot(query: str):
    # STEP 1 — Retrieve context
    docs = vs.similarity_search(query, k=4)
    context = "\n\n".join([d.page_content for d in docs])

    # STEP 2 — Construct final prompt
    prompt = f"""
You are Rowan University's information assistant.

Context from Rowan official data:
{context}

Answer the following question clearly using ONLY the above data:

Question: {query}
"""

    # STEP 3 — Call LLM correctly for LangChain 0.3+
    response = llm.invoke([HumanMessage(content=prompt)])

    # STEP 4 — Return final text
    return response.content
