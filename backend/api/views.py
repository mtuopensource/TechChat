from rest_framework import status, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets, generics
from .models import Board, Thread, User, Post, Participant
from .serializers import BoardSerializer, ThreadSerializer, UserSerializer, PostSerializer, ParticipantSerializer
from .permissions import IsAdminOrReadOnly

class BoardViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = BoardSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # Set of all Boards
    def get_queryset(self):
        return Board.objects.all()

    # List of Threads related to the specified Board.
    @detail_route(methods=['get'], suffix='Threads')
    def threads(self, request, id=None):
        queryset = Thread.objects.filter(board=id)
        serializer = ThreadSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

# Allows a Thread to be created, retrieved, and destroyed.
class ThreadViewSet(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView, viewsets.GenericViewSet):
    lookup_field = 'id'
    serializer_class = ThreadSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # Set of all Threads
    def get_queryset(self):
        return Thread.objects.all()

    # Disable list of all Threads for performance reasons.
    def list(self, request):
        content = {'detail': 'Method "GET" not allowed.'}
        code = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(content, status=code)

class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)

    # Set of all Boards
    def get_queryset(self):
        return User.objects.all()
        
    @list_route(methods=['get', 'post'], permission_classes = ())
    def login(self, request):
        username = None
        password = None

        # Location of the username and password depends on the method
        if request.method == 'GET':
            if 'email' in request.GET and 'password' in request.GET: # Check if the username and password was provided
                username = request.GET['email']
                password = request.GET['password']
            else:
                content = {'detail': 'Insufficient information'} # TODO Constant Response
                code = status.HTTP_400_BAD_REQUEST
                return Response(content, status=code)
        elif request.method == 'POST':
            if 'email' in request.POST and 'password' in request.POST: # Check if the username and password was provided
                username = request.POST['email']
                password = request.POST['password']
            else:
                content = {'detail': 'Insufficient information'} # TODO Constant Response
                code = status.HTTP_400_BAD_REQUEST
                return Response(content, status=code)

        queryset = User.objects.filter(email=username).filter(password=password) # Set of User objects with the given email and password
        serializer = UserSerializer(queryset, context={'request': request}, many=True)

        # Does not exist
        if not serializer.data:
            content = {'detail': 'The credentials you provided cannot be determined to be authentic.'} # TODO Constant Response
            code = status.HTTP_401_UNAUTHORIZED
            return Response(content, status=code)
        else:
            content = {'detail': 'Success'} # TODO Constant Response
            code = status.HTTP_200_OK
            return Response(content, status=code)

class PostViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # Set of all Boards
    def get_queryset(self):
        return Post.objects.all()

class ParticipantViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = ParticipantSerializer
    permission_classes = (IsAdminOrReadOnly,)
    #Set of all Boards
    def get_queryset(self):
        return Participant.objects.all()
