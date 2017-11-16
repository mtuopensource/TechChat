from rest_framework_mongoengine import viewsets
from .models import Board
from .serializers import BoardSerializer

class BoardViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = BoardSerializer
    
    def get_queryset(self):
        return Board.objects.all()
