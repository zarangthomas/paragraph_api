from django.db import models
from django.contrib.auth import get_user_model 
import uuid
from django.contrib.auth import get_user_model 

word_index = {} 

def update_word_index(paragraph_text):  # Encapsulated index updating
    words = paragraph_text.split()  
    for word in words:
        if word in word_index:
            word_index.get(word).append(paragraph_text.id)
        else:
            word_index[word] = [paragraph_text.id] 

class Paragraph(models.Model):
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=100, unique=True) 

    def save(self, *args, **kwargs):
        if not self.unique_id:  
            self.unique_id = str(uuid.uuid4())  
        super().save(*args, **kwargs)
        update_word_index(self.text)  

