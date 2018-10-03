from api.models import Comment
from api.permissions import IsOwnerOrReadOnly
from api.serializers import CommentSerializer
from api.views import CreateRetrieveUpdateDestroy
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(CreateRetrieveUpdateDestroy):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        ip = self.get_client_ip(self.request)
        serializer.save(author=self.request.user, ip=ip)
