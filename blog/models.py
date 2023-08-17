from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


# esta clase es de cada articulo/post
class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now) #cambiar 'timestamp' a 'fecha'
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return self.content