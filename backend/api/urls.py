from api.views import BoardViewSet, PostViewSet, CommentViewSet, UserViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'posts', PostViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token/$', TokenObtainPairView.as_view()),
    url(r'^token/refresh/$', TokenRefreshView.as_view()),
]
