from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import detail_route, list_route
from api.models import User
from api.serializers import UserSerializer

# Users can be created, updated, and destroyed.
# Users cannot be listed or retrieved for security reasons.
class UserViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    lookup_field = 'id'

    # Set of all Users
    def get_queryset(self):
        return User.objects.all()

    # Returns 200 OK           if the credentials were correct
    # Returns 401 UNAUTHORIZED if the credentials were invalid
    # Returns 400 BAD REQUEST  if the credentials were not provided
    # @see https://docs.djangoproject.com/en/2.0/topics/http/sessions/
    @list_route(methods=['get', 'post'], permission_classes = ())
    def login(self, request):
        return User.login_manager.login(request)

    # Ends any existing sessions.
    # Returns 200 OK
    # @see https://docs.djangoproject.com/en/2.0/topics/http/sessions/
    @list_route(methods=['get', 'post'], permission_classes = ())
    def logout(self, request):
        return User.login_manager.logout(request)
