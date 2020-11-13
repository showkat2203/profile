from django.shortcuts import render
from portfolio.models import Project, Post, Comment

def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog-detail.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog-detail.html", context)