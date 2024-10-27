from django.urls import path

from RegularExam.common import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
)