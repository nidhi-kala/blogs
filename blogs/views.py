from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'blogs/index.html', {'posts': posts})


def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view_post', post_id=post.id)

    return render(request, 'blogs/view_post.html', {'post': post, 'comments': comments, 'form': form, })


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blogs/create_post.html', {'form': form})
