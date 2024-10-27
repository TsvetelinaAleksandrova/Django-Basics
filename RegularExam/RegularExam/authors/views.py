from django.shortcuts import render, redirect

from RegularExam.authors.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from RegularExam.posts.models import Post
from RegularExam.utils import get_profile


def create_profile(request):
    profile = get_profile()
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,

    }

    return render(request, 'author/create-author.html', context)


def details_profile(request):
    profile = get_profile()
    post_count = Post.objects.filter(author=profile).count()
    last_post = Post.objects.filter(author=profile).order_by('-updated_at').first()

    context = {
        'profile': profile,
        'post_count': post_count,
        'last_post': last_post,
    }
    return render(request, 'author/details-author.html', context)


def edit_profile(request):
    profile = get_profile()
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():

            form.save()

            return redirect('details-profile')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'author/edit-author.html', context)


def delete_profile(request):
    profile = get_profile()

    form = DeleteProfileForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'author/delete-author.html', context)