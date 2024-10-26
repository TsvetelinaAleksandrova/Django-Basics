from django.urls import path

from SpeedApp.common import views

urlpatterns = (
    path('', views.index_page, name='index'),
)