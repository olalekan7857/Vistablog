from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import ReviewForm, CommentForm
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def index(request):
    posts = Post.objects.order_by('-id')[:15]
    cats = Categories.objects.all()
    context = {
        'posts':posts,
        'categories':cats
    }
    return render(request, 'index.html', context )

def about(request):
    missions = Mission.objects.order_by('-id')[:1]
    profiles = Profile.objects.order_by('-id')[:1]
    Acknowledgements = Acknowledgement.objects.order_by('-id')[:1]

    context = {
        'missions':missions,
        'profiles':profiles,
        'Acknowledgements':Acknowledgements
    }
    return render(request, 'about.html', context)


def error(request):
    return render(request, '404.html')

def contact(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send the email
            send_mail(
                subject=f"New Message from {name}: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            # Now save the form to the database
            form.save()

            messages.success(request, "Your message was sent successfully.")
            return redirect('Vistablog:contact')
    else:
        form = ReviewForm()

    context = {'form':form}
    return render(request, 'contact.html', context)


def postpage(request, slug):
    myslug = Post.objects.get(slug = slug)
    comments = myslug.comments.all()
    new_comments = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comments = form.save(commit=False)
            new_comments.post = myslug
            new_comments.save()
            return HttpResponseRedirect(reverse('Vistablog:postpage', args= [str(myslug.slug)]))
    else:
        form = CommentForm()
    
    comment_count = comments.count()


    category = myslug.category.name
    mycategory = Categories.objects.get(name = category)
    category_posts = Post.objects.filter(category = mycategory).order_by('-id')[:3]

    return render(request, 'singlepost.html', locals(), )

def category(request, category):
    mycategory = Categories.objects.get(slug = category)
    posts = Post.objects.filter(category = mycategory)

    context = {
        'posts':posts,
        'category':mycategory
    }
    return render(request, 'category.html', context)