from app import openai, prompts, classification


def get_answer(prompt, model, transcript, template):
    print("prompt in get-answer")
    print(prompt)
    answer = "nothing in transformerhub"
    if template == "legislation-parse":
        print("template triggered")
        pre_prompt = prompts.legislation_prompt
        print(pre_prompt)
        prompt['user_message'] = pre_prompt + prompt['user_message']
    
    if model == "DistilBERT-base":
        print("sentiment")
        answer = classification.bert_base(prompt)
        print("answer in transformer: ", answer)

        
    if model == "gpt3.5":
        answer = openai.chat3turbo(prompt, transcript)
    
    if model == "gpt4":
        answer = openai.chat4(prompt, transcript)
        print ("gpt4 response in transformer")

        
    return answer