from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.home, name = "home"), 
    path('prompt/', views.prompt, name = "prompt"), 
    path('whatsapp/', views.send_whatsapp, name = "whatsapp")
]
