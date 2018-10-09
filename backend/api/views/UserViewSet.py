from api.permissions import IsOwnerOrReadOnly
from api.serializers import UserSerializer
from api.views import CreateRetrieveUpdateDestroy
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class UserViewSet(CreateRetrieveUpdateDestroy):
    """
    Simple ViewSet for creating, retrieving, updating, and destroying Users.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        permission_classes = []
        if not self.action == 'create':
            permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
        return [permission() for permission in permission_classes]
