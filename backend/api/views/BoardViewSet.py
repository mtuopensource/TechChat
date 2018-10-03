from api.models import Board, Post
from api.serializers import BoardSerializer, PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class BoardViewSet(ReadOnlyModelViewSet):
    """
    Simple ViewSet for listing or retrieving Boards.
    """
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

    @action(detail=True)
    def posts(self, request, *args, **kwargs):
        """
        Return:
            HttpResponse containing Posts associated with the given Board.
        """
        board = self.get_object()
        posts = Post.objects.filter(board=board)
        post_serializer = PostSerializer(posts, many=True)
        return Response(post_serializer.data)
