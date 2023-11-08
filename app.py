# Q&A chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os 

load_dotenv()  # load environment variables from the .env file

# Function to load OpenAI model and get responses

def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"), model_name = "text-davinci-003", temperature = .5)
    response = llm(question)
    return response


## initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input: ", key='input')
response = get_openai_response(input)

submit = st.button("Ask the question")

if submit:
    st.subheader("The response is ")
    st.write(response)
