from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone

def post_list(request):
    posts = Post.objects.order_by('-pk')
    return render(request, 'main/post_list.html', {"title": "softquoké", "posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {"title": "post detail", "post": post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request, 'main/post_new.html', {'title': 'new post', 'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
        return render(request, 'main/post_edit.html', {"title": "post edit", "form": form, "pk": pk})
		
def post_delet(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')