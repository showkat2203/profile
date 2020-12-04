from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.core.mail import send_mail, BadHeaderError
from portfolio.models import Project, Post, Comment
from portfolio.forms import CommentForm, ContactForm

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

# def blog_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     comments = Comment.objects.filter(post=post)
#     context = {
#         "post": post,
#         "comments": comments,
#     }

#     return render(request, "blog-detail.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        import pdb
        pdb.set_trace()
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['chysonnet@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render(request, 'index.html', {'form': form})
    return render(request, 'index.html', {'form': form})