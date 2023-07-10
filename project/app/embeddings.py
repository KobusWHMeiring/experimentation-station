import pandas as pd
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
import pinecone
import openai
from tqdm.auto import tqdm  # this is our progress bar
import uuid
import re



#langchain's embeddings model setup

def parse_pdf(doc_url):
    #parses the pdf by page
    loader = PyPDFLoader(doc_url)
    raw_doc = loader.load()
    """  cleaned_docs = []
    for doc in raw_doc:
        doc_str = str(doc)
        cleaned_text = re.sub(r"\n+", " ", doc_str)  # Remove consecutive newlines
        cleaned_text = re.sub(r"\s{2,}", " ", cleaned_text)  # Replace multiple spaces with a single space
 
        
        cleaned_docs.append(cleaned_text) """
    

    return(raw_doc)
   

def split_text(raw_doc):
    recursive_text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap  = 200,
        length_function = len,
        add_start_index = True,
    )
    recursive_docs = recursive_text_splitter.split_documents(raw_doc)

    
    return(recursive_docs)

def embed(index_name, recursive_docs):
    index_name = 'experimentation-station'
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    #creating pinecone connection 
    pinecone.init(      
    	api_key=os.getenv("pinecone_api_key"),      
    	environment='asia-southeast1-gcp-free'      
    )      
    #okay so this line below creates the index in one go somehow...  Not really a fan of how seperated I am from the code here.
    created_index = Pinecone.from_documents(recursive_docs, embeddings, index_name=index_name) 
    return(created_index)




def search_doc(query):
    pinecone.init(      
    	api_key=os.getenv("pinecone_api_key"),      
    	environment='asia-southeast1-gcp-free'      
    )      
    index_name = "experimentation-station"
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    
    print("search doc triggered")
    
    
    
    print('docsearch declared')
    query = query
    print("query in here")
    user_message = query["user_message"]
    docs = docsearch.similarity_search(user_message)
    print("relevant docs")
    print(docs)
    return(docs)
