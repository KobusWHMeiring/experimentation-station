from app.models import Session, Messages, Chat, ChatMessages
from django.core.exceptions import ObjectDoesNotExist


def initialise():
    
    
    newChat = Session.objects.create()
    
    print("new chat initialised")
    print (newChat)
    
    return newChat


def add_message(guid, prompt, role, model):
    
    session = Session.objects.get(guid = guid)
    content = prompt['user_message']
    
    save_me = Messages.objects.create(
        session = session,
        content = content,
        function = "not_implemented",
        role = role,
        model = model,
    )
    save_me.save()
    
    
    
def add_whatsapp(id, prompt, content, role):
    
    
    try:
        chat = Chat.objects.get(chat_id=id)
        save_me = ChatMessages.objects.create(
        chat = chat,
        content = content,
        prompt = prompt,
        role = role,
        )
        save_me.save()
    except ObjectDoesNotExist:
        print("Chat not found with message_id:", id)
        print("new chat started")
        newChat = Chat.objects.create(
            chat_id = id,
            cell = "0799140837" #TODO find this data
        )
        save_me = ChatMessages.objects.create(
            chat = newChat,
            content = content,
            prompt = prompt,
            role = role,
            )
        save_me.save()
    
    