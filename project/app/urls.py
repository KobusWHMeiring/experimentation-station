from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.home, name = "home"), 
    path('prompt/', views.prompt, name = "prompt"), 
    path('upload/', views.upload, name = "upload"), 
    path('whatsapp/', views.send_whatsapp, name = "whatsapp"),
    path('receive-whatsapp/', views.receive_whatsapp, name = "receive")
]
