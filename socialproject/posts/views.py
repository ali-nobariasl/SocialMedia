from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm
from .models import PostModel
from django.contrib.auth.decorators import login_required


login_required(login_url='user_login')
def create_post(request):
    if request.method == 'POST':
        my_form = PostForm(request.POST, files=request.FILES)
        if my_form.is_valid():
          new_post = my_form.save(commit=False)
          new_post.user = request.user
          new_post.save()
          #return HttpResponse('post created successfully')  
    else:
        my_form = PostForm()
    context  = {
        'form': my_form,
    }
    return render(request, 'posts/create.html', context=context)
