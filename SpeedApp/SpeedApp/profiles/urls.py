from django.urls import path

from SpeedApp.profiles import views

urlpatterns = (
    path('create/', views.create_profile_page, name='create-profile'),
    path('details/', views.car_details_page, name='details-profile'),
    path('edit/', views.edit_profile_page, name='edit-profile'),
    path('delete/', views.delete_profile_page, name='delete-profile'),
)