from django.http import HttpResponse
from django.shortcuts import render

from djangoProject.todo_app.models import Task


def index(request):
    title_filter = request.GET.get('title_filter', '')

    tasks = Task.objects.filter(name__icontains=title_filter)

    context = {
        'title_filter': title_filter,
        'all_tasks': tasks,
    }

    return render(request, 'tasks/index.html', context=context)


def add_view(request):
    return HttpResponse("<h1>Add view</h1>")