from rest_framework.viewsets import ReadOnlyModelViewSet 
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models.Board import Board
from api.models.Post import Post
from api.serializers.BoardSerializer import BoardSerializer
from api.serializers.PostSerializer import PostSerializer

class BoardViewSet(ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    @action(methods=['get'], detail=True)
    def posts(self, request, *args, **kwargs):
        board = self.get_object()
        query = Post.objects.filter(board = board)
        serial = PostSerializer(query, many = True) 
        return Response(serial.data)