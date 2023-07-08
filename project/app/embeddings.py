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



#langchain's embeddings model setup


def embed(index_name, doc_url):
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

    recursive_text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap  = 200,
        length_function = len,
        add_start_index = True,
    )

    #so it looks like we can go straight from pdf which is very helpful.  Will be using langchains loaddocument function, and they are using the pypdf library
    loader = PyPDFLoader(doc_url)
    raw_doc = loader.load()
    recursive_docs = recursive_text_splitter.split_documents(raw_doc)

    #ffs, okay so this output type is a lanchain Document which means the standard pinecone ingesting/upserting doesn't work and we have to use langchain's method
    print(type(recursive_docs[1]))

    
    #creating pinecone connection 
    pinecone.init(      
    	api_key='1367b533-cc04-4b08-9274-eeea672dbf0f',      
    	environment='asia-southeast1-gcp-free'      
    )      
    index = pinecone.Index(index_name)

    index_name = index_name
   
    
    #okay so this line below creates the index in one go somehow...  Not really a fan of how seperated I am from the code here.
    created_index = Pinecone.from_documents(recursive_docs, embeddings, index_name=index_name) 




def search_doc(query):
    pinecone.init(      
    	api_key='1367b533-cc04-4b08-9274-eeea672dbf0f',      
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
