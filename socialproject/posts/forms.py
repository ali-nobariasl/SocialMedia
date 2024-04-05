from django import forms
from .models import PostModel,Commment


class PostForm(forms.ModelForm):
    class Meta:
        model= PostModel
        fields = {'title','content','image'}
        

class CommentForm(forms.ModelForm):
    class Meta:
        model= Commment
        fields = {'body','posted_by',}