from django.db import models
import uuid

# Create your models here.


class Session(models.Model):
    guid = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "hello"
    
    
class Messages(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    content = models.TextField(max_length=200000)
    role = models.CharField(max_length=200) 
    model = models.CharField(max_length=200)
    function = models.CharField(max_length=200, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        words = self.content.split()[:10]  # Split the content into words and take the first 10
        truncated_content = ' '.join(words)  # Join the first 10 words back into a string
        return truncated_content
    
    def transcript(self):
        messages = []
        related_messages = Messages.objects.filter(session=self).order_by('time_stamp')
        
        for message in related_messages:
            if message.role == 'system':
                messages.append({"role": "system", "content": message.content})
            else:
                messages.append({"role": "user", "content": message.content})
        
        return messages
