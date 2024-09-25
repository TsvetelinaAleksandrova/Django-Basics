from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.pet_add_page, name='pet_add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page, name='pet_details'),
        path('edit/', views.pet_edit_page, name='pet_edit'),
        path('delete/', views.pet_delete_page, name='pet_delete'),
    ]))
]