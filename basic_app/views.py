from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'basic_app/post_list.html', {'posts': posts})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post)
    return render(request, 'basic_app/post_details.html', {'post': post})


def creat_post(request):
    
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post = post.save()
            return redirect('post_details', pk = post.pk)
    else:
        form = PostForm()

    return render(request, 'basic_app/creat_post.html', {"form": form})    

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance= post)
        if form.is_valid():
            post = form.save()
            return redirect('post_details', pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'basic_app/creat_post.html', {"form": form})   

def delet_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete() 
    return redirect('home')