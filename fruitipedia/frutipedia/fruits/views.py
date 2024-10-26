from django.shortcuts import render, redirect

from frutipedia.fruits.forms import DeleteFruitForm, EditFruitForm, CreateFruitForm
from frutipedia.fruits.models import Fruit
from frutipedia.utils import get_user_obj


def add_fruit(request):
    profile = get_user_obj()
    form = CreateFruitForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = get_user_obj()

    context = {
        'fruit': fruit,
        'profile': profile,

    }
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    profile = get_user_obj()

    form = EditFruitForm(instance=fruit)
    if request.method == 'POST':
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form,
        'profile': profile,
    }
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    profile = get_user_obj()
    fruit = Fruit.objects.get(id=fruit_id)

    form = DeleteFruitForm(instance=fruit)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form,
        'profile': profile,
    }
    return render(request, 'fruits/delete-fruit.html', context)





