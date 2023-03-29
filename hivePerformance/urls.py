from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wellnessTool/', include('wellnessTool.urls')),
    path('', include('dashboard.urls')),
]
