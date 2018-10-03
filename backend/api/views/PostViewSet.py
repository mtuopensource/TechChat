from api.models import Post, Comment
from api.permissions import IsOwnerOrReadOnly
from api.serializers import PostSerializer, CommentSerializer
from api.utils import get_client_ip
from api.views.CreateRetrieveUpdateDestroy import CreateRetrieveUpdateDestroy
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class PostViewSet(CreateRetrieveUpdateDestroy):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        ip = get_client_ip(self.request)
        serializer.save(author=self.request.user, ip=ip)

    @action(detail=True)
    def comments(self):
        post = self.get_object()
        query = Comment.objects.filter(post=post)
        serial = CommentSerializer(query, many=True)
        return Response(serial.data)
