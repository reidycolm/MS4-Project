from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def blog_post(request, slug):
    post = Post.objects.get(slug=slug)
    template = 'blog/blog_details.html'
    context = {
        'post': post,
    }

    return render(request, template, context)

