import torch
from transformers import AdamW, AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset


raw_datasets = load_dataset("glue", "mrpc")

""" 
This is the long way to tokenize your sentences for trianing.
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
tokenized_sentences_1 = tokenizer(raw_datasets["train"]["sentence1"])
tokenized_sentences_2 = tokenizer(raw_datasets["train"]["sentence2"])

Can be done in one go by just passing the sentence - token_outputs = Tokenizer(first sentence, second sentence, padding = true, truncation = true)
BUT the above approach runs everything you are passing into the tokenizer through the RAM, so you can get memory issues.  Proposed is that you use a map function rather
def tokenize(example):
    return(tokenizer(example["sentence1"], example["sentence2"])) (if you put padding = true in this section, it will pad every sentece in the dataset
    to be of the same length.  This can be a waste when the majority of the sentences aren't as long as the longest one.  It is advised to rather pad the
    batches dynamically. Slightly more complex code, here it is: 
    
    from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer=tokenizer))
    
tokenized_datasets = raw_datasets.map(tokenize, batched=True)
 """
checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
    
    
sequences = [
    "I've been waiting for a HuggingFace course my whole life.",
    "This course is amazing!",
]


batch = tokenizer(sequences, padding=True, truncation=True, return_tensors="pt")


# This is new
batch["labels"] = torch.tensor([1, 1])

optimizer = AdamW(model.parameters())
loss = model(**batch).loss
loss.backward()
optimizer.step()