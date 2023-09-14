from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import DataRowViewSet, table_view

router = DefaultRouter()
router.register(r'rows', DataRowViewSet)

urlpatterns = [
    path('', table_view, name='table_view'),
    path('api/', include(router.urls)),
]
