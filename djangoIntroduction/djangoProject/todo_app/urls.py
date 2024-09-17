from django.urls import path

from djangoProject.todo_app.views import index, add_view

urlpatterns = [
    path('', index),
    path('add/',add_view),
]
