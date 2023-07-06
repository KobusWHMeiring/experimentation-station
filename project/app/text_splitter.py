from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter


with open('../CPA.txt') as f:
    legislation = f.read()

#might be worth looking at more deeply if there are specific things in the act to split by.
#char_text_splitter = CharacterTextSplitter(        
#    separator = "/n ",
#    chunk_size = 2000,
#    chunk_overlap  = 50,
#   length_function = len,
#)


recursive_text_splitter = RecursiveCharacterTextSplitter(
    
    chunk_size = 2000,
    chunk_overlap  = 300,
    length_function = len,
    add_start_index = True,
)
#char_texts = char_text_splitter.create_documents([state_of_the_union])

recursive_texts = recursive_text_splitter.create_documents([legislation])

#Consistent splits, but does chop sentences.  Making overlap bigger does help though
print("recursive_splitter")
print(recursive_texts[0])
print(recursive_texts[1])

