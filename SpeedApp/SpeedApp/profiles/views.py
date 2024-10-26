from django.db.models import Sum
from django.shortcuts import render, redirect

from SpeedApp.cars.models import Car
from SpeedApp.profiles.forms import ProfileBaseForm, EditProfileForm, DeleteProfileForm
from SpeedApp.utils import get_profile


def create_profile_page(request):
    form = ProfileBaseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}

    return render(request, template_name='profile/profile-create.html', context=context)


def car_details_page(request):
    profile = get_profile()
    total_cars_price = Car.objects\
        .filter(owner=profile, owner__isnull=False)\
        .aggregate(total_price=Sum('price'))['total_price'] or 0

    context = {
        'profile': profile,
        'total_cars_price': total_cars_price
    }

    return render(request, template_name='profile/profile-details.html', context=context)


def edit_profile_page(request):
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
    return render(request, 'profile/profile-edit.html', context)


def delete_profile_page(request):
    profile = get_profile()
    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)
