from django.shortcuts import render

# Create your views here.

def home(request):
    
    context = {"name": "Kobus"}
    return render(request, "app/index.html", context)