from app import openai


def get_answer(prompt, model, transcript):

    
    if model == "gpt3.5":
        answer = openai.chat3turbo(prompt, transcript)
        
        
    return answer