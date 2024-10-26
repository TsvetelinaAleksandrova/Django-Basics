from django.shortcuts import render

from SpeedApp.profiles.models import Profile


def index_page(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, template_name='common/index.html', context=context)