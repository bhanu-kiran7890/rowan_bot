# rag.py
from langchain_community.document_loaders import PyPDFLoader, TextLoader  # type: ignore
from langchain_community.vectorstores import FAISS  # type: ignore
from langchain_community.embeddings import OllamaEmbeddings  # type: ignore
import os

DOCS_DIR = "app/data/"

def load_all_docs():
    docs = []
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            path = os.path.join(root, file)
            if file.endswith(".pdf"):
                documents = PyPDFLoader(path).load()
                docs.extend(documents)
            elif file.endswith(".txt"):
                documents = TextLoader(path).load()
                docs.extend(documents)
    return docs

def build_vector_store():
    print("Loading documents...")
    docs = load_all_docs()
    print(f"Loaded {len(docs)} documents.")

    # 👉 FAST, LIGHTWEIGHT EMBEDDINGS
    # (No freezing, safe for all laptops)
    print("Creating embeddings using nomic-embed-text...")
    embeddings = OllamaEmbeddings(model="llama3")

    print("Building FAISS vectorstore... This will be fast.")
    vs = FAISS.from_documents(docs, embeddings)

    print("Saving vectorstore...")
    vs.save_local("app/vectorstore")

    print("Vectorstore built successfully!")
    return vs

def load_vector_store():
    print("Loading existing vectorstore...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return FAISS.load_local("app/vectorstore", embeddings, allow_dangerous_deserialization=True)

