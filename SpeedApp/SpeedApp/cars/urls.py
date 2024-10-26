from django.urls import path, include

from SpeedApp.cars import views

urlpatterns = (
    path('catalogue/', views.catalogue_page, name='catalogue'),
    path('create/', views.create_car_page, name='create-car'),
    path('<int:pk>/', include([
        path('details/', views.car_details_page, name='details_car'),
        path('edit/', views.edit_car_page, name='edit_car'),
        path('delete/', views.delete_car_page, name='delete_car'),
    ]))
)