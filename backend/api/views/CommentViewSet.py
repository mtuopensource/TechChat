from api.models import Comment
from api.permissions import IsOwnerOrReadOnly
from api.serializers import CommentSerializer
from api.views import CreateRetrieveUpdateDestroy
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(CreateRetrieveUpdateDestroy):
    """
    Simple ViewSet for creating, retrieving, updating, and destroying Comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]  # destructive actions require ownership and authentication
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """
        Saves the User's UUID and IP address.
        Parameters:
            serializer: CommentSerializer used to create Comment.
        """
        ip = self.get_client_ip(self.request)
        serializer.save(author=self.request.user, ip=ip)
