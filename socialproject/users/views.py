from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


def user_login(request):
    if request.method == "POST":
        myform = LoginForm(request.POST) 
        if myform.is_valid():
            username = myform.cleaned_data["username"]
            password = myform.cleaned_data["password"]
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)  
                user.is_active = True
                return HttpResponse("user logged in successfully")  
            else:
                return HttpResponse("Invalid username or password")  
    else: 
        myform = LoginForm() 
        
    context ={'form': myform}
    return render(request,'users/login.html',context=context)


def user_logout(request):

    logout(request)
    return render(request,'users/logout.html')


@login_required(login_url='user_login')
def index(requset):
    
    return render(requset,'users/index.html')

def user_register(requset):
    if requset.method == 'POST':
        myform = RegisterForm(requset.POST)
        if myform.is_valid():
            name = myform.cleaned_data['username']
            password = myform.cleaned_data['password']
            email = myform.cleaned_data['email']
            user = User(username=name, password=password, email=email)
            user.is_active = True
            user.save()
            print('saved')
        else:
            return HttpResponse('Invalid username or password')    
    else:
        myform = RegisterForm()
    
    context = {'myform':myform}
    return render(requset,'users/register.html',context=context)