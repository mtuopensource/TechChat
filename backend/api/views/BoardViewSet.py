from rest_framework_mongoengine.viewsets import ModelViewSet
from api.models import Board, Thread
from api.serializers import BoardSerializer, ThreadSerializer
from api.permissions import IsAdminOrReadOnly

# Threads can be listed, created, retrieved, updated, and destroyed.
class BoardViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,) # Only allow admins to create, update, destroy
    serializer_class = BoardSerializer
    lookup_field = 'id'

    # Set of all Boards
    def get_queryset(self):
        return Board.objects.all()

    # When viewing a Board's details, display a list of associated Threads.
    def retrieve(self, request, id=None):
        context = {
            'request': request # Used to determine ip, author
        }
        serializer = ThreadSerializer(Thread.objects.filter(board=id), context=context, many=True)
        return Response(serializer.data)
