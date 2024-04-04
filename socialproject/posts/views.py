from django.http import HttpResponse 
from django.shortcuts import render , redirect
from .forms import PostForm
from .models import PostModel
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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


def feed(request):
    posts = PostModel.objects.all()
    profile = Profile.objects.all()
    logged_user = request.user
    context = {'posts': posts,
               'profile': profile,
               'logged_user': logged_user}
    return render(request, 'posts/feed.html',context=context)


def like_post(request, pk):
    
    post = get_object_or_404(PostModel, id=pk)
    
    if request.user in post.liked_by.all():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
       
    context= {}
    
    return redirect('feed')

