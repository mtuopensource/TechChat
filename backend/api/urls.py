from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.views.BoardViewSet import BoardViewSet
from api.views.PostViewSet import PostViewSet
from api.views.CommentViewSet import CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'boards', BoardViewSet, r'board')
router.register(r'posts', PostViewSet, r'post')
router.register(r'comments', CommentViewSet, r'comment')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token/$', TokenObtainPairView.as_view()),
    url(r'^token/refresh/$', TokenRefreshView.as_view()),
]
