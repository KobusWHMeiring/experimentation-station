from app import openai, managedata


def firstMessage(message, id):
    
    prompt = {'user_message': message, 'system_message': "You are a bot working for teampact your name is fin. Please respond to this person with a question to figure out what they need help with."}
   
    message = openai.chat3turbo(prompt, "")
    return (message)