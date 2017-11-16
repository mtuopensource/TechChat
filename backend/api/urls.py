from django.conf.urls import url, include
from rest_framework import routers
from .views import BoardViewSet

# DRF router for REST API viewsets
router = routers.DefaultRouter()

# Register endpoints with DRF router
router.register(r'board', BoardViewSet, r"board")

urlpatterns = [
    url(r'^', include(router.urls, namespace='api')),
]
