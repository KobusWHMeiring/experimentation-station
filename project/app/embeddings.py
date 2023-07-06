import pandas as pd
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.text_splitter import CharacterTextSplitter

#Using the recursive splitter at 2000 chunk size and some overlap for now, if I can find a better seperator I'll go for that later.
#char_text_splitter = CharacterTextSplitter(        
#    separator = "Part ",
#    chunk_size = 2000,
#    chunk_overlap  = 50,
#    length_function = len,
#)

recursive_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 2000,
    chunk_overlap  = 200,
    length_function = len,
    add_start_index = True,
)


embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191


#so it looks like we can go straight from pdf which is very helpful.  Will be using langchains loaddocument function, and they are using the pypdf library
loader = PyPDFLoader("../PAIA.pdf")
raw_doc = loader.load()




recursive_docs = recursive_text_splitter.split_documents(raw_doc)

print("recursive_docs")
print(recursive_docs)






