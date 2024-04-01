from typing import Iterable
from django.db import models
from users.models import Profile
from django.conf import settings



class PostModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    content = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='/posts/%y/%m/%d/')
    slug = models.SlugField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self):
        
        return super().save(force_insert, force_update, using, update_fields)
    
