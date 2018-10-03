from api.viewsets.CreateRetrieveUpdateDestroy import CreateRetrieveUpdateDestroy
from api.models.Comment import Comment
from api.serializers.CommentSerializer import CommentSerializer
from api.permissions.IsOwnerOrReadOnly import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from api.utils import get_client_ip


class CommentViewSet(CreateRetrieveUpdateDestroy):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        ip = get_client_ip(self.request)
        serializer.save(author=self.request.user, ip=ip)
