from django.shortcuts import render
from app import transformerhub
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from app import managedata, whatsapp, teamhelper
from app.models import Messages, Session
import json
# Create your views here.

def home(request):
    
    session = managedata.initialise()
    context = {
        "guid": session.guid
        }
    return render(request, "app/index.html", context)


@csrf_exempt
def receive_whatsapp(request):
    if request.method == 'POST':
        payload = json.loads(request.body.decode('utf-8'))
        try:
            entry = payload['entry'][0]
            print(payload)
            changes = entry['changes'][0]
            value = changes['value']
            if 'messages' in value:
                messages = value['messages']
                if messages:
                    text_body = messages[0]['text']['body']
                    conversation_id = messages[0]['id']
                    response = teamhelper.convoHelper(text_body, conversation_id)
                    send_whatsapp(response)
            else:
                print("No messages found in the payload.")  
                print(payload) 
                id_value = value['statuses'][0]['id']
                print(id_value)
        except (KeyError, IndexError) as e:
            print(f"Error accessing payload: {e}")
    payload = json.loads(request.body.decode('utf-8'))
    
    if request.method == 'GET':
        verify_token = 'thetokenforverification'  # Set your verify token here
        hub_mode = request.GET.get('hub.mode')
        hub_challenge = request.GET.get('hub.challenge')
        hub_verify_token = request.GET.get('hub.verify_token')

        if hub_mode == 'subscribe' and hub_verify_token == verify_token:
            print("hub mode success!")
            return HttpResponse(hub_challenge, content_type='text/plain', status=200)
            
        else:
            return HttpResponse(status=403)
    


    return HttpResponse(request)

@csrf_exempt
def send_whatsapp(request):
    
    """ message = request.POST.get('message', "Hello World") """
    message = request

    """ await whatsapp.send_message(message) """
    whatsapp.non_async_send(message)
    
   
    back = {"status": "ge-send"}
    
    return(HttpResponse(back))
    
    
    


@csrf_exempt
def prompt(request):
    #whatever the user asked
    prompt = request.POST.get('prompt', None)
    #This field is always there Question-answer, not present for other prompt types.
    system_message =  request.POST.get('system_prompt', "")
    model = request.POST.get('model', None)
    guid = request.POST.get('guid', None)
    #either "standard question" or "legislation parse"
    template = request.POST.get('template', None)
    session = Session.objects.get(guid = guid)
    transcript = Messages.transcript(session)
    
    role = "User"
    
    if system_message:
        prompt = {"user_message":prompt,"system_message":system_message}
    else: 
        prompt = {"user_message":prompt}
   
    #need to check if this works for the whatsapp chats
    managedata.add_message(guid, prompt, role, model)
    
    answer = transformerhub.get_answer(prompt, model, transcript, template)
    
    role = "System"
    prompt = {"user_message":answer,"system_message":"NA"}
    managedata.add_message(guid, prompt, role, model)
    
    response = {"answer": answer}
    
    return JsonResponse(response)
    
    
    
    
    