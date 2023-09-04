from django.db import models
from datetime import datetime

class Login(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    age=models.IntegerField(max_length=3)
    description=models.TextField()
    author=models.CharField(max_length=50)
    created_at=models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.name
    
