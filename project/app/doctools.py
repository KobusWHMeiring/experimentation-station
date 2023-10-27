import re
from langchain.document_loaders import PyPDFLoader
from pypdf import PdfReader
import pandas as pd
import csv
from langchain.text_splitter import RecursiveCharacterTextSplitter
import sys, pathlib, fitz

def clean_content(list_o_sentences):
    return_doc = []
    for i in range(0, len(list_o_sentences)):
        cleaned_text = re.sub(r"\n+", " ", str(list_o_sentences[i]))  # Remove consecutive newlines
        cleaned_text = re.sub(r"\s{2,}", " ", cleaned_text)  # Replace multiple spaces with a single space
        cleaned_text = re.sub(r"\.{2,}", ".", cleaned_text)
        cleaned_text = cleaned_text.replace('\ufb01', '')
        return_doc.append(cleaned_text)
          
    return(return_doc)


def get_content(list_o_sentences):
    start_index = list_o_sentences.index("page_content='") + len("page_content='")
    end_index = list_o_sentences.index("' metadata=")
    page_content = list_o_sentences[start_index:end_index]
    return(page_content)    


def get_metadata(list_o_sentences):
    metadata_start_index = list_o_sentences.index("metadata={'") + len("metadata={'")
    metadata_end_index = list_o_sentences.index("}'", metadata_start_index)
    metadata = list_o_sentences[metadata_start_index:metadata_end_index]

def parse_pdf(doc_url):
    #parses the pdf by page, saves the page data and the metadata as two items in an object.
    loader = PyPDFLoader(doc_url)
    raw_doc = loader.load()
    return(raw_doc)


def parse_pdf2(doc_url):
    doc =fitz.open(doc_url)
    out = open("output.txt", "wb")
    for page in doc: 
        text = page.get_text().encode(utf8)
     
    return(text)
    
    
def split_text(raw_doc):
    
    recursive_text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap  = 200,
        length_function = len,
        add_start_index = True,
    )
    recursive_docs = recursive_text_splitter.split_documents(raw_doc)

    
    return(recursive_docs)


def write_text_to_csv(data):
    with open("test", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
        
        
def write_list_to_csv(filename, operation, data_list):
    if operation == "replace":
        operation = "w"
    elif operation == "new":
        operation = "x"
    else: 
        operation = "a"
    with open(filename, operation, newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in data_list:
            writer.writerow([item])
    print(f"CSV With title: {filename} has been created")

def read_csv_as_df(filename):
    df = pd.read_csv(filename, index_col=0)
    df.head(2)
    print(df.head(2))

def write_content_and_metadata(input_list): 
    output_file = "newfile"
    f = open(output_file, 'w', newline='')
        
    for item in input_list:
        start_index = item.index("page_content='") + len("page_content='")
        end_index = item.index("' metadata=")
        page_content = item[start_index:end_index]
        metadata_start_index = item.index("metadata={'") + len("metadata={'")
        metadata_end_index = item.index("}'", metadata_start_index)
        metadata = item[metadata_start_index:metadata_end_index] 
        output_file = "output.csv"
        writer = csv.writer(f)
        writer.writerow(['Page Content', 'Metadata'])
        writer.writerow([page_content, metadata])   
            
            
def write_list_to_txt(filename, operation, data_list):
    if operation == "replace":
        operation = "w"
    elif operation == "new":
        operation = "x"
    else: 
        operation = "a"
    f = open(filename, operation)
    
    for embed in data_list:
        embed_string = str(embed)
        f.write(embed_string)
    f.close()


def get_text_after_word(text, word):
    index = text.find(word)
    if index != -1:
        return text[index + len(word):]
    else:
        return None
    
def remove_slashes(text):
    return text.replace('/', '')