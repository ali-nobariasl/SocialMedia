from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from .models import Profile

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



def user_register(request):
    if request.method == 'POST':
        myform = RegisterForm(request.POST)
        if myform.is_valid():
            #name = myform.cleaned_data['username']
            #password = myform.cleaned_data['password']
            #email = myform.cleaned_data['email']
            #user = User(username=name, password=password, email=email)
            #user.is_active = True
            #user.save()
            new_user  = myform.save(commit=False)
            new_user.set_password(myform.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'users/register_done.html')
        else:
            return HttpResponse('Invalid username or password')    
    else:
        myform = RegisterForm()
    
    context = {'myform':myform}
    return render(request,'users/register.html',context=context)



def edit(request):
    if request.method == 'POST':
        pass
    else:
        pass
    context = {}
    return render(request,'users/edit.html',context=context)