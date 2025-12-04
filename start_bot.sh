from pathlib import Path

# Path where the script will be saved
script_path = Path("/mnt/data/start_bot.sh")

# Script content based on user's workspace setup
script_content = """#!/bin/bash
echo "🔁 Starting Rowan Info Bot..."

# Navigate to project directory
cd /workspace/rowan_bot

# Activate virtual environment
echo "📦 Activating Python virtual environment..."
source ../venv/bin/activate

# Kill any running ollama processes
echo "🧹 Stopping any running Ollama instances..."
pkill -f ollama

# Start Ollama in background
echo "🚀 Starting Ollama server..."
ollama serve &

# Launch FastAPI app
echo "🌐 Launching FastAPI app..."
python app/main.py
"""

# Write script file
script_path.write_text(script_content)

# Make it executable
script_path.chmod(0o755)

script_path.name
