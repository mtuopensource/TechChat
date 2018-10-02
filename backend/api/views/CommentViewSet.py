from rest_framework.viewsets import GenericViewSet 
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from api.models.Comment import Comment
from api.serializers.CommentSerializer import CommentSerializer
from api.permissions.IsOwnerOrReadOnly import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from ..utils import get_client_ip

class CommentViewSet(RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        ip = get_client_ip(self.request)
        serializer.save(author = self.request.user, ip = ip)
