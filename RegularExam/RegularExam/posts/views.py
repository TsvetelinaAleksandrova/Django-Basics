from django.shortcuts import render, redirect

from RegularExam.posts.forms import CreatePostForm, EditPostForm, DeletePostForm
from RegularExam.posts.models import Post
from RegularExam.utils import get_profile


def create_post(request):
    profile = get_profile()
    form = CreatePostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = profile
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'posts/create-post.html', context)


def details_post(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = get_profile()

    context = {
        'post': post,
        'profile': profile,

    }
    return render(request, 'posts/details-post.html', context)


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = get_profile()

    form = EditPostForm(instance=post)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'post': post,
        'form': form,
        'profile': profile,
    }
    return render(request, 'posts/edit-post.html', context)


def delete_post(request, post_id):
    profile = get_profile()
    post = Post.objects.get(id=post_id)

    form = DeletePostForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    context = {
        'post': post,
        'form': form,
        'profile': profile,
    }

    return render(request, 'posts/delete-post.html', context)