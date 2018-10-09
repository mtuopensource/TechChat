from api.models import Post, Comment
from api.permissions import IsOwnerOrReadOnly
from api.serializers import PostSerializer, CommentSerializer
from api.views.CreateRetrieveUpdateDestroy import CreateRetrieveUpdateDestroy
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PostViewSet(CreateRetrieveUpdateDestroy):
    """
    Simple ViewSet for creating, retrieving, updating, and destroying Posts.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]  # destructive actions require ownership and authentication
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        """
        Saves the User's UUID and IP address.
        Parameters:
            serializer: PostSerializer used to create Post.
        """
        ip = self.get_client_ip(self.request)
        serializer.save(author=self.request.user, ip=ip)

    @action(detail=True)
    def comments(self, request, *args, **kwargs):
        """
        Return:
            HttpResponse containing Comments associated with the given Post.
        """
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        comment_serializer = CommentSerializer(comments, many=True)
        return Response(comment_serializer.data)
