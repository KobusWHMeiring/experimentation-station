from app.models import Session, Messages

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