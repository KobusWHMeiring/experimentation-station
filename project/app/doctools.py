import re
from langchain.document_loaders import PyPDFLoader
import pinecone
import csv
from langchain.text_splitter import RecursiveCharacterTextSplitter

def clean_content(list_o_sentences):
    return_doc = []
    for i in range(0, len(list_o_sentences)):
        cleaned_text = re.sub(r"\n+", " ", str(list_o_sentences[i]))  # Remove consecutive newlines
        cleaned_text = re.sub(r"\s{2,}", " ", cleaned_text)  # Replace multiple spaces with a single space
        cleaned_text = re.sub(r"\.{2,}", ".", cleaned_text)
        return_doc.append(cleaned_text)
          
    return(return_doc)

def parse_pdf(doc_url):
    #parses the pdf by page
    loader = PyPDFLoader(doc_url)
    raw_doc = loader.load()
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


def write_list_to_csv(filename, data_list):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in data_list:
            writer.writerow([item])
    print(f"CSV With title: {filename} has been created")
            
            
            
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