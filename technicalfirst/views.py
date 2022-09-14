import re
from urllib import request
from django.shortcuts import render, redirect
from .models import Post, Subscriber, Comment, Contact
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .forms  import SubscribeForm

# Home Page
def home(request):
    if request.method == 'POST':
        # if Subscriber.objects.filter(Email=email).exists():
        #     messages.info(request, 'Already Subscribed')
        #     return redirect('/')
        # else:
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
        # subscribe = Subscriber(Name=name, Email=email)
        # subscribe.save()
            messages.success(request, 'Subscribe Successfully')
        return redirect('/')
    blog = Post.objects.all().order_by('-post_key')[:2]
    return render(request, 'pages/index.html', {'blog': blog})

# About Page


def about(request):
    return render(request, 'pages/about.html')

# Contact Page


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Connect = Contact(Name=name, Email=email,
                          subject=subject, messages=message)
        Connect.save()
        messages.success(
            request, 'Your message has been received, We will contact you soon.')
    return render(request, 'pages/contact.html')

# Privacy Page


def privacy(request):
    return render(request, 'pages/privacy.html')

# Disclaimer


def disclaimer(request):
    return render(request, 'pages/disclaimer.html')

# Post View Page


def post(request, post_slug):
    if request.method == 'POST':
        name = request.POST['name']
        msg = request.POST['msg']
        post_ids = request.POST['post_key']

        addComment = Comment(
            post_id=post_ids, comment_name=name, comment_msg=msg)
        addComment.save()
        messages.success(request, 'Comment Added Successfully')

    post = Post.objects.filter(post_slug=post_slug)[0]
    return render(request, 'pages/post.html', {'post': post})

# Subscriber Api


@login_required(login_url='/admin')
def subscribers(request):
    data = list(Subscriber.objects.values())
    return JsonResponse(data, safe=False)
