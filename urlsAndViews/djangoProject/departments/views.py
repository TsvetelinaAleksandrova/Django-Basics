from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from djangoProject.departments.admin import Department
from djangoProject.departments.models import Departments


def index(request):
    return HttpResponse("Hello World!")


# def view_with_name(request, *args, **kwargs):
#     return HttpResponse(f"<h1>Args: {args} Kwargs: {kwargs}</h1>")


def view_with_name(request, variable): #should be named the same way as in the url
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, 'departments/name_template.html', {"variable": variable})


def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int pkp with pk: {pk}</h1>")


def view_with_slug(request, pk, slug):
    # OPTION 1 for 404
    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404

    # OPTION 2
    department = get_object_or_404(Department, pk=pk, slug=slug)

    raise Http404

    #return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg/')


def redirect_to_view(request):
    # redirect('http://localhost:8000/numbers/')  breaks abstraction
    # redirect(index)   # breaks single responsibility if view is from another app
    return redirect('home')  # Best option