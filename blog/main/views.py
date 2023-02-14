from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'main/post_list.html', {"title": "softquoké", "posts": posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/post_detail.html', {"title": "post detail", "post": post})