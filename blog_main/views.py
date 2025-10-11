from django.http import HttpResponse
from django.shortcuts import render

from about.models import About
from blogs.models import Blog, Category
from django.db.models import Q


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
