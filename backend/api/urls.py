from django.conf.urls import url, include
from rest_framework import routers
from .views import BoardViewSet, ThreadViewSet

# DRF router for REST API viewsets
router = routers.DefaultRouter()

# Register endpoints with DRF router
router.register(r'boards', BoardViewSet, r"board")
router.register(r'threads', ThreadViewSet, r"thread")

urlpatterns = [
    url(r'^', include(router.urls, namespace='api')),
]
