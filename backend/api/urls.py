from django.conf.urls import url, include
from rest_framework import routers
from api.views import BoardViewSet, ThreadViewSet, UserViewSet, PostViewSet, ParticipantViewSet

# DRF router for REST API viewsets
router = routers.DefaultRouter()

# Register endpoints with DRF router
router.register(r'boards', BoardViewSet, r"board")
router.register(r'threads', ThreadViewSet, r"thread")
router.register(r'users', UserViewSet, r"user")
router.register(r'posts', PostViewSet, r"post")
router.register(r'participants', ParticipantViewSet, r"participant")

urlpatterns = [
    url(r'^', include((router.urls, 'api'), namespace='api'))
]
