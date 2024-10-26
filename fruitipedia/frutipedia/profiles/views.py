from django.shortcuts import render, redirect

from frutipedia.fruits.models import Fruit
from frutipedia.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from frutipedia.utils import get_user_obj


def create_profile(request):
    profile = get_user_obj()
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,

    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = get_user_obj()
    post_count = Fruit.objects.filter(owner=profile).count()

    context = {
        'profile': profile,
        'post_count': post_count,

    }
    return render(request, 'profiles/details-profile.html', context)


def edit_profile(request):
    profile = get_user_obj()

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
    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = get_user_obj()

    form = DeleteProfileForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/delete-profile.html', context)


