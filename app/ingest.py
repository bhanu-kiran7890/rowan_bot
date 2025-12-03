from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitters import RecursiveCharacterTextSplitter

import os

# Load documents from app/docs/
docs_path = "app/data"
all_docs = []

for file in os.listdir(docs_path):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(docs_path, file))
        all_docs.extend(loader.load())

# Split texts into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(all_docs)

# Use HuggingFace embeddings (or replace with another if needed)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create and save FAISS index
db = FAISS.from_documents(documents, embeddings)
db.save_local("app/vectorstore")

print("✅ FAISS vectorstore created at app/vectorstore")
