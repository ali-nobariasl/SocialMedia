from typing import Iterable
from django.db import models
from users.models import Profile
from django.conf import settings
from django.utils.text import slugify


class PostModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    content = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/%y/%m/%d/')
    slug = models.SlugField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='posts_liked', blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
