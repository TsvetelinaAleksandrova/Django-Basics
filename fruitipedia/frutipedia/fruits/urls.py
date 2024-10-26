from django.urls import path, include

from frutipedia.fruits import views

urlpatterns = (
    path('create/', views.add_fruit, name='add-fruit'),
    path('<int:fruit_id>/', include([
        path('details/', views.details_fruit, name='details-fruit'),
        path('edit/', views.edit_fruit, name='edit-fruit'),
        path('delete/', views.delete_fruit, name='delete-fruit'), ]
    ))
)
