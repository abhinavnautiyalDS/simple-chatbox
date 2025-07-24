# Install dependencies (Run this in terminal, not inside the script)
pip install -r requirements.txt

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Set up the Hugging Face endpoint
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"  # Changed from "conversational" to valid task
)

# Wrap with ChatHuggingFace
model = ChatHuggingFace(llm=llm)

# Streamlit app UI
st.header("RESEARCH TOOL")
user_input = st.text_input("Enter your prompt")

if st.button("Summarise"):
    result = model.invoke(user_input)
    st.write(result.content)
