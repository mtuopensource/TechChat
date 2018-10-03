from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet 


class CreateRetrieveUpdateDestroy(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                                  GenericViewSet):
    pass
