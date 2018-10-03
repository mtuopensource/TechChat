from api.views.CreateRetrieveUpdateDestroy import CreateRetrieveUpdateDestroy
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models.Post import Post
from api.models.Comment import Comment
from api.serializers.PostSerializer import PostSerializer
from api.serializers.CommentSerializer import CommentSerializer
from api.permissions.IsOwnerOrReadOnly import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from api.utils import get_client_ip


class PostViewSet(CreateRetrieveUpdateDestroy):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        ip = get_client_ip(self.request)
        serializer.save(author=self.request.user, ip=ip)

    @action(methods=['get'], detail=True)
    def comments(self):
        post = self.get_object()
        query = Comment.objects.filter(post=post)
        serial = CommentSerializer(query, many=True)
        return Response(serial.data)

