from app import openai


def get_answer(user_message, system_message, model):
    print(user_message)
    print(system_message)
    prompt = {"user_message":user_message,
              "system_message":system_message}
    transcript = [""]
    
    if model == "gpt3.5":
        answer = openai.chat3turbo(prompt)
        print("answer in transfromers")
        print(answer)
        
    return answer