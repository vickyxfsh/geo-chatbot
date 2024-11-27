import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

st.title("Chatbot")

with st.form("llm-form"):
    text = st.text_input("Enter your question")
    submit_button = st.form_submit_button("Submit")


def generate_response(text):
    try:
        llm = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434")
        response = llm.invoke(text)
        print("Response received:", response.content)
        return response.content
    except Exception as e:
        print("Error invoking model:", e)
        return "There was an error processing your request."

if submit_button:
    if text:
        response = generate_response(text)
        st.write(response)
    else:
        st.write("Please enter a question.")

if submit_button and text:
    with st.spinner("Generating response..."):
        response = generate_response(text)
        st.session_state["chat_history"].append({"question": text, "response": response})
        st.write(response)

st.write("Chat History")
for chat in reversed(st.session_state["chat_history"]):
    st.write(f"User: {chat['user']}")
    st.write(f"Assistant: {chat['ollama']}")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

