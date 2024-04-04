from django.urls import path

from .views import create_post, feed


urlpatterns = [

    path('create/', create_post, name='create'),
    path('feed/', feed, name='create'),
    

] 