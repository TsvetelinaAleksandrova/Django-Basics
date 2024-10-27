from django.shortcuts import render

from RegularExam.utils import get_profile, get_all_posts


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, template_name='index.html', context=context)


def dashboard(request):
    profile = get_profile()
    posts = get_all_posts()
    context = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'dashboard.html', context)
