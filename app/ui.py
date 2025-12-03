import streamlit as st
import requests

# -----------------------------
# FASTAPI BACKEND URL
# -----------------------------
API_URL = "http://127.0.0.1:8000/ask"

# -----------------------------
# STREAMLIT CONFIG
# -----------------------------
st.set_page_config(page_title="Rowan Info Bot", page_icon="📘", layout="centered")

st.title("📘 Rowan Info Bot")
st.write("Ask me anything about Rowan University!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg, sender in st.session_state.messages:
    if sender == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 RowanBot:** {msg}")

# Input box
query = st.text_input("Enter your question:")

# When user submits
if st.button("Ask") or (query and st.session_state.get("enter_pressed")):
    if query:
        # Add to history
        st.session_state.messages.append((query, "user"))

        # Send request to FastAPI backend
        try:
            response = requests.get(API_URL, params={"query": query})
            if response.status_code == 200:
                answer = response.json().get("answer", "No response")
            else:
                answer = "Error: Could not reach the backend."

        except Exception as e:
            answer = f"Backend error: {str(e)}"

        # Add bot response
        st.session_state.messages.append((answer, "bot"))

        # Clear input
        st.experimental_rerun()
