
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frutipedia.common.urls')),
    path('fruit/', include('frutipedia.fruits.urls')),
    path('profile/', include('frutipedia.profiles.urls')),
]
