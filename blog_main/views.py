from django.http import HttpResponse
from django.shortcuts import redirect, render

from about.models import About
from .forms import RegistrationForm
from blogs.models import Blog, Category
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib import messages


def home(request):
    featured_posts = Blog.objects.filter(
        is_featured=True, status='Published').order_by("?")
    print(featured_posts)

    posts = Blog.objects.filter(
        is_featured=False, status='Published')
    print(posts)

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)


def aboutUs(request):
    aboutus = About.objects.first()
    context = {
        'aboutus': aboutus,
    }
    return render(request, 'about.html', context)


def searchblog(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(
        short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Something went wrong! Please try again")
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')

            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
