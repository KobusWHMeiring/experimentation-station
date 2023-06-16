from app import openai


def get_answer(prompt, model, transcript):
    
    if model == "gpt3.5":
        answer = openai.chat3turbo(prompt, transcript)
    
    if model == "gpt4":
        answer = openai.chat4(prompt, transcript)
        print ("gpt4 response in transformer")

        
        
    return answer