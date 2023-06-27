from app import openai, managedata
from app.models import Chat, ChatMessages


def convoHelper(message, id):
    transcript = ""
    try:
        print("id in convohelper")
        print(id)
        example = Chat.objects.get(id = 1)
        print("example id")
        print(example.chat_id)
        chat = Chat.objects.get(chat_id=id)
        transcript = ChatMessages.transcript(chat)
        print("transcript in convohelper")
        print (transcript)
    except Chat.DoesNotExist:
        # Handle the case where the Chat object doesn't exist
        print("Chat object not found with ID:", id)
        
   
    
    prompt = {'user_message': message, 'system_message': "You are a bot working for teampact your name is fin. Please respond to this person with a question to figure out what they need help with."}
    role = "User"
    
    managedata.add_whatsapp(id, prompt, message, role)
    
    message = openai.chat3turbo(prompt, transcript)
    print("message from chat3turbo")
    print(message)
    role = "ConvoSystem"
    
    prompt = {"user_message":message,"system_message":"NA"}
    content = message
    managedata.add_whatsapp(id, prompt, content, role)
    
    return (message)