from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from api.models import Thread, Post
from api.serializers import ThreadSerializer, PostSerializer
from api.permissions import IsOwnerOrAdmin

# Threads can be created, retrieved, updated, and destroyed.
# Threads cannot be listed for performance reasons.
class ThreadViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = (IsOwnerOrAdmin,) # Allow Thread authors to update or destroy
    serializer_class = ThreadSerializer
    lookup_field = 'id'

    # Set of all Threads
    def get_queryset(self):
        return Thread.objects.all()

    # When viewing a Thread's details, display a list of associated Posts.
    def retrieve(self, request, id=None):
        context = {
            'request': request # Used to determine ip, author
        }
        postSerializer = PostSerializer(Post.objects.filter(thread=id), context=context, many=True)
        threadSerializer = ThreadSerializer(Thread.objects.filter(id=id), context=context, many=True)
        threadSerializer.data[0]['posts'] = postSerializer.data
        return Response(threadSerializer.data[0])
