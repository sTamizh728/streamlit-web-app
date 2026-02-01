import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
import requests
from bs4 import BeautifulSoup

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

st.set_page_config(page_title="AI ChatBot", layout="wide")
st.title("Search the web AI (Gemma:2b)")

with st.sidebar:
    st.header("settings")
    site_url = st.text_input("Enter site URL")
    procerss_button = st.button("proces url")

llm = Ollama(model="gemma:2b")
embedding = OllamaEmbeddings(model="gemma:2b")

if procerss_button and site_url:
    with st.spinner("Processing the site."):
        loder = WebBaseLoader(site_url)
        document = loder.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        final_document = text_splitter.split_documents(document)

        vectorstore = Chroma.from_documents(
            documents=final_document,
            embedding=embedding
        )
        st.session_state.retriever = vectorstore.as_retriever()
        st.success("Site processed successfully.")

## Prompt Template
prompt = ChatPromptTemplate.from_template("""
Answer the following question only based on the provided context.
If the answer is not in provided say "I Cannot find the answer from the provided website URL."
<context>
{context}
</context>
Question: {input}
""")

## Streamlit framework
if "retriever" in st.session_state:
    st.title("Langchain Demo With Gemma Model")
    user_input = st.text_input("Tell What you want to know?")

    if user_input:
        with st.spinner("Searching the answer"):
            # Get relevant documents
            docs = st.session_state.retriever.invoke(user_input)
            
            # Format context from documents
            context = "\n\n".join([doc.page_content for doc in docs])
            
            # Create the chain and get response
            chain = prompt | llm | StrOutputParser()
            response = chain.invoke({"context": context, "input": user_input})
            
        st.markdown("Answer:")
        st.write(response)