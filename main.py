import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file, including OpenAI API key

# Set up the Streamlit page configuration
st.set_page_config(page_title="NewsBot: News Research Tool 📈", page_icon="📰")

# Title and sidebar setup
st.title("NewsBot: News Research Tool 📈📰🌐📊🔍")
st.sidebar.title("News Article URLs 📎🗞️🔗🌍📰")

# Input fields for up to 3 URLs in the sidebar
st.sidebar.markdown("### Enter up to 3 URLs of news articles to analyze: 📰🌐🔗📎🗞️")
urls = [st.sidebar.text_input(f"URL {i+1}", placeholder="Enter URL here...") for i in range(3)]

# Button to trigger the processing of URLs
if st.sidebar.button("Process URLs"):
    if any(urls):  # Check if at least one URL is provided
        with st.spinner("Loading data from URLs... 🌐🔄📥📰📎"):
            loader = UnstructuredURLLoader(urls=urls)  # Load documents from provided URLs
            data = loader.load()

        with st.spinner("Splitting text into chunks..."):
            text_splitter = RecursiveCharacterTextSplitter(
                separators=['\n\n', '\n', '.', ','],  # Define separators for chunking text
                chunk_size=1000  # Maximum chunk size in characters
            )
            docs = text_splitter.split_documents(data)  # Split documents into chunks

        with st.spinner("Creating embeddings and building vector store..."):
            embeddings = OpenAIEmbeddings()  # Initialize embeddings
            vectorstore_openai = FAISS.from_documents(docs, embeddings)  # Create a FAISS vector store from the documents

        # Save the FAISS index to a pickle file for later use
        with open("faiss_store_openai.pkl", "wb") as f:
            pickle.dump(vectorstore_openai, f)
        st.sidebar.success("URLs processed successfully! ✅📎🌐📰🔍")
    else:
        st.sidebar.error("Please enter at least one URL. 🌐📎🗞️🔗📥")

# Input field for user query
query = st.text_input("Enter your question here: ❓🖊️📥🌐📋")
if query:
    if os.path.exists("faiss_store_openai.pkl"):  # Check if the FAISS index file exists
        with open("faiss_store_openai.pkl", "rb") as f:
            vectorstore = pickle.load(f)  # Load the FAISS vector store
            chain = RetrievalQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0.9, max_tokens=500), retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)  # Get the answer to the query

            st.header("Answer")
            st.write(result["answer"])  # Display the answer

            # Display the sources used for the answer
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split sources by newline
                for source in sources_list:
                    st.write(source)  # Display each source
    else:
        st.error("FAISS index not found. Please process URLs first. 📊🔍🗂️🌐📎")
