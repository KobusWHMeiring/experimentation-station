import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def bert_base(prompt):
    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
    input_text = prompt['user_message']
    
    
   
    tokens = tokenizer(input_text, padding=True, truncation=True, return_tensors="pt")
    
    
    output_logits = model(**tokens).logits
    print("output in classification", output_logits)
    
    predicted_class_id = output_logits.argmax().item()
    post_processed = model.config.id2label[predicted_class_id]
    print(post_processed)
    
   
    return post_processed
    
    """    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    model.config.id2label[predicted_class_id] """