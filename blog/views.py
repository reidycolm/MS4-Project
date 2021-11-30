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


def edit_blog_post(request, post_id):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only Admins can edit a blog post')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            form.save()
            messages.success(request, 'Blog Post Updated!')
            return redirect(reverse('blog_post', args=[post.slug]))
        else:
            messages.error(request,
                           'Could not add your post to the site. \
                           Please ensure form is valid!')
    else:
        form = PostForm(instance=post)

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


def delete_blog_post(request, post_id):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only Admins can delete a blog post')
        return redirect(reverse('home'))
    
    blog = get_object_or_404(Post, pk=post_id)
    blog.delete()
    messages.success(request, 'Blog Post deleted!')

    return redirect(reverse('blog'))
