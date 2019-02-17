from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('landingarea.urls')),  
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
