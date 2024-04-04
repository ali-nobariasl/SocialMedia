from django.urls import path

from .views import create_post, feed, like_post


urlpatterns = [

    path('create/', create_post, name='create'),
    path('feed/', feed, name='feed'),
    path('like/<int:pk>', like_post, name='like'),
    

] 