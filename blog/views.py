from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib import messages


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


def add_blog_post(request):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only Admins can create a new blog post')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            messages.success(request, 'Successfully added a New Blog Post!')
            return redirect(reverse('blog_post', args=[post.slug]))
        else:
            messages.error(request,
                           'Could not add your new post to the site. \
                           Please ensure form is valid!')
    else:
        form = PostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
