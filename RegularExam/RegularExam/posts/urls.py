from django.urls import path, include

from RegularExam.posts import views

urlpatterns = (
    path('create/', views.create_post, name='create-post'),
    path('<int:post_id>/', include([
        path('details/', views.details_post, name='details-post'),
        path('edit/', views.edit_post, name='edit-post'),
        path('delete/', views.delete_post, name='delete-post'),
        ]
    ))
)