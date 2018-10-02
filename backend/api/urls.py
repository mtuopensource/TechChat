from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views.BoardViewSet import BoardViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet, r'board')

urlpatterns = [
    url(r'^', include(router.urls)),
]