from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from api.models import Post
from api.serializers import PostSerializer
from api.permissions import IsOwnerOrAdmin

# Posts can be created, retrieved, updated, and destroyed.
# Posts cannot be listed for performance reasons.
class PostViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = (IsOwnerOrAdmin,) # Allow Post authors to update or destroy
    serializer_class = PostSerializer
    lookup_field = 'id'

    # Set of all Posts
    def get_queryset(self):
        return Post.objects.all()
