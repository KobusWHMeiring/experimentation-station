from django.contrib import admin
from app.models import Chat, ChatMessages, Messages, Session
# Register your models here.

admin.site.register(Chat)
admin.site.register(Session)
admin.site.register(ChatMessages)
admin.site.register(Messages)