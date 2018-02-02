from rest_framework import status, permissions, mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets, generics
from api.models import Board, Thread, User, Post, Participant
from .serializers import BoardSerializer, ThreadSerializer, UserSerializer, PostSerializer, ParticipantSerializer
from .permissions import IsAdminOrReadOnly, TechChatIsAuthenticated, TechChatIsAdminOrReadOnly, TechChatIsOwnerOrAdmin
from .response import INSUFFICIENT_INFORMATION, SUCCESS, NOT_AUTHORIZED

class BoardViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = BoardSerializer
    permission_classes = (TechChatIsAdminOrReadOnly,)
    queryset=Board.objects.all()

    # List of Threads related to the specified Board.
    def retrieve(self, request, id=None):
        queryset = Thread.objects.filter(board=id)
        serializer = ThreadSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

# Allows a Thread to be created, retrieved, updated, and destroyed.
class ThreadViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    lookup_field = 'id'
    serializer_class = ThreadSerializer
    permission_classes = (TechChatIsOwnerOrAdmin,)
    queryset=Thread.objects.all()

    # List of Posts related to the specified Thread.
    def retrieve(self, request, id=None):
        queryset = Post.objects.filter(thread=id)
        serializer = PostSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

class PostViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    lookup_field = 'id'
    serializer_class = PostSerializer
    permission_classes = (TechChatIsOwnerOrAdmin,)
    queryset=Post.objects.all()




























class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UserSerializer
    # permission_classes = (IsAdminOrReadOnly,)

    # Set of all Boards
    def get_queryset(self):
        return User.objects.all()

    def destroy(self, request, id=None):
        operand     = User.objects.get(id=id) # The user which might be deleted
        credentials = User.login_manager.get_credentials_from_request(request)
        response    = User.login_manager.login(request) # Check if the credentials are valid
        if response.status_code == SUCCESS.status_code:
            if operand.email == credentials.get('username'):
                # OK to remove own profile
                # TODO FLAG AS HIDDEN, RATHER THAN DELETE
                return super(viewsets.ModelViewSet, self).destroy(request, id)
            else:
                return NOT_AUTHORIZED.as_response() # Not OK to remove someone else's profile
        else:
            return response

    # Disable list of all Users for security reasons.
    def list(self, request):
        content = {'detail': 'Method "GET" not allowed.'}
        code = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(content, status=code)

    # Disable retrieval of individual user data for security reasons.
    def retrieve(self, request, id=None):
        content = {'detail': 'Method "GET" not allowed.'}
        code = status.HTTP_405_METHOD_NOT_ALLOWED
        return Response(content, status=code)

    @list_route(methods=['get', 'post'], permission_classes = ())
    def logout(self, request):
        del request.session['techchat_userid']
        request.session.modified = True
        return SUCCESS.as_response()

    @list_route(methods=['get', 'post'], permission_classes = ())
    def login(self, request):
        return User.login_manager.login(request)



class ParticipantViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = ParticipantSerializer
    permission_classes = (IsAdminOrReadOnly,)
    #Set of all Boards
    def get_queryset(self):
        return Participant.objects.all()
