from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_check.urls')),
    path('table/', include('table.urls')),
]
