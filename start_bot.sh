#!/bin/bash

echo "🔁 Activating virtual environment..."
source venv/bin/activate

echo "🧠 Starting Ollama server in background..."
ollama serve > /dev/null 2>&1 &

echo "📦 Pulling LLaMA3 model (if not already pulled)..."
ollama pull llama3

echo "📚 Building vectorstore..."
python app/ingest.py

echo "🚀 Starting Rowan Bot FastAPI server..."
python app/main.py
