from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields={'username', 'email','first_name'}
    
    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('password is incorrect')
        return self.cleaned_data['password']
    
    
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = {'photo',}
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model= User
        fields = {'first_name', 'email','last_name'}