from api.models import Board, Post
from api.serializers import BoardSerializer, PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class BoardViewSet(ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    @action(detail=True)
    def posts(self):
        board = self.get_object()
        query = Post.objects.filter(board=board)
        serial = PostSerializer(query, many=True)
        return Response(serial.data)
