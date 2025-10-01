from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog, Category


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
