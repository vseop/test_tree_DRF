from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TreeViewSet

router = DefaultRouter()
router.register(r'tree', TreeViewSet)
urlpatterns = [
    path('', include(router.urls))
]
