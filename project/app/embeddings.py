import pandas as pd

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import os
import pinecone
import openai
from tqdm.auto import tqdm  # this is our progress bar
import uuid
import re
from app import doctools



#langchain's embeddings model setup

def embed_pinecone(index_name, recursive_docs):
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

def embed_openai(docs):
    text = ""
    for doc in docs:
        text += doc
    model="text-embedding-ada-002"
    return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']





def search_doc_pinecone(query):
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
