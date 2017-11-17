from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets, generics
from .models import Board, Thread
from .serializers import BoardSerializer, ThreadSerializer

@login_required
class BoardViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = BoardSerializer

    # Set of all Boards
    def get_queryset(self):
        return Board.objects.all()

    # List of Threads related to the specified Board.
    @detail_route(methods=['get'], suffix='Threads')
    def threads(self, request, id=None):
        threads = Thread.objects.filter(board=id)
        serializer = ThreadSerializer(threads, context={'request': request}, many=True)
        return Response(serializer.data)

# Allows a Thread to be created, retrieved, and destroyed.
class ThreadViewSet(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView, viewsets.GenericViewSet):
    lookup_field = 'id'
    serializer_class = ThreadSerializer

    # Set of all Threads
    def get_queryset(self):
        return Thread.objects.all()

    # Disable list of all Threads for performance reasons.
    def list(self, request):
        content = {'detail': 'Method "GET" not allowed.'}
        code = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(content, status=code)
