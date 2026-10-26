import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Gemini Chatbot", layout="wide")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME = "models/gemini-2.5-flash"  # ✅ WORKS WITH YOUR KEY

st.title("🤖 Gemini Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.history.append(("user", user_input))

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_input
    )

    st.session_state.history.append(("assistant", response.text))

for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.write(msg)
