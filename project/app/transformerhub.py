from app import openai, prompts, classification, embeddings


def get_answer(prompt, model, transcript, template):
    
    answer = "nothing in transformerhub"
    
    if template == "legislation-parse":
        print("template triggered")
        pre_prompt = prompts.legislation_prompt
        
        prompt['user_message'] = pre_prompt + prompt['user_message']
        prompt['system_message'] = prompts.legislation_system_prompt
        
    if template == 'query-legislation':
        print("leg query")
        context = embeddings.search_doc(prompt)
        context_str = str(context)
        print('prompt in get_answer')
        print(prompt)
        user_message = prompt['user_message']
        #it's ugly, but i'm going to amend the prompt here otherwise I have to change the chat3turbo function just to deal with this edge case
        prompt['user_message'] = "A user is asking a question of some legislation.  This is the user's question: " + user_message + " This is the relevant sections of legislation: " + context_str + ". Please explain the legislation and then answer the user's question."
        print(prompt)
        
    if model == "DistilBERT-base":
        print("sentiment")
        answer = classification.bert_base(prompt)
        print("answer in transformer: ", answer)
 
    if model == "gpt3.5":
        answer = openai.chat3turbo(prompt, transcript)
        print(answer)
    
    if model == "gpt4":
        answer = openai.chat4(prompt, transcript)
        print ("gpt4 response in transformer")

        
    return answer