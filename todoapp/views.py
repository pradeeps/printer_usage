from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request, 'todoapp/home-page.html', context)

def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)
    context = {
    'post': post
    }
    return render(request, 'todoapp/post_detail.html', context)
