from django.shortcuts import render
from app import transformerhub
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
# Create your views here.

def home(request):
    
    context = {"name": "Kobus"}
    return render(request, "app/index.html", context)


@csrf_exempt
def prompt(request):
    prompt = request.POST.get('prompt', None)
    system_message = request.POST.get('model', "you are j krishnamurti")
    model = request.POST.get('model', None)
    answer = transformerhub.get_answer(prompt,system_message, model)
    response = {"answer": answer}
    
    return JsonResponse(response)
    
    
    
    
    