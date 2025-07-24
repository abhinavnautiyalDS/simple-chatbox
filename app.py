# This block runs in Python, not in requirements.txt
import os

# Install dependencies only once
if not os.path.exists(".installed_dependencies"):
    os.system("pip install -r requirements.txt")
    open(".installed_dependencies", "w").close()

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

# ✅ Correct: load .env file (the argument must be a string path)
load_dotenv(".env")

# Set up the Hugging Face endpoint
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"  # Ensure the model supports this task
)

# Wrap with ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# Streamlit app UI
st.header("RESEARCH TOOL")
user_input = st.text_input("Enter your prompt")

if st.button("Summarise"):
    result = model.invoke(user_input)
    st.write(result.content)
