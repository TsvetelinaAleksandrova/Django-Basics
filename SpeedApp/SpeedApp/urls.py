
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SpeedApp.common.urls')),
    path('car/', include('SpeedApp.cars.urls')),
    path('profile/', include('SpeedApp.profiles.urls')),
]
