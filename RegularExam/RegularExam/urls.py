
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RegularExam.common.urls')),
    path('posts/', include('RegularExam.posts.urls')),
    path('author/', include('RegularExam.authors.urls')),
]
