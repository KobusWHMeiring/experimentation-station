from django.shortcuts import render
from app import transformerhub
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from app import managedata
from app.models import Messages, Session
# Create your views here.

def home(request):
    
    session = managedata.initialise()
    context = {
        "guid": session.guid
        }
    return render(request, "app/index.html", context)


@csrf_exempt
def prompt(request):
    prompt = request.POST.get('prompt', None)
    system_message =  request.POST.get('system_prompt', "")
    model = request.POST.get('model', None)
    guid = request.POST.get('guid', None)
    template = request.POST.get('template', None)
    session = Session.objects.get(guid = guid)
    transcript = Messages.transcript(session)
    
    role = "User"
    
    prompt = {"user_message":prompt,"system_message":system_message}
   
    managedata.add_message(guid, prompt, role, model)
    
    answer = transformerhub.get_answer(prompt, model, transcript, template)
    role = "System"
    prompt = {"user_message":answer,"system_message":"NA"}
    managedata.add_message(guid, prompt, role, model)
    
    response = {"answer": answer}
    
    return JsonResponse(response)
    
    
    
    
    