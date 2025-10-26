from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category, Comment

# Create your views here.


def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category_id=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('404.html')

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=single_blog)
    count = comments.count()
    print(comments)
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'count': count,
    }
    return render(request, 'blogs.html', context)
