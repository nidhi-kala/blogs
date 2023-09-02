from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'blogs/index.html', {'posts': posts})


def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blogs/view_post.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.isvalid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blogs/create_post.html', {'form': form})
