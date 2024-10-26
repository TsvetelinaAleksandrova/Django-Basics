from django.shortcuts import render

from frutipedia.utils import get_user_obj, get_all_fruits


def index(request):
    profile = get_user_obj()
    context = {'profile': profile}
    return render(request, template_name='index.html', context=context)


def dashboard(request):
    profile = get_user_obj()
    fruits = get_all_fruits()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'fruits/../../templates/dashboard.html', context)
