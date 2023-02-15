from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.order_by('-pk')
    return render(request, 'main/post_list.html', {"title": "softquoké", "posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {"title": "post detail", "post": post})

def post_new(request):
    form = PostForm()
    return render(request, 'main/post_new.html', {'title': 'new post', 'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_edit.html', {"title": "post edit", "post": post})