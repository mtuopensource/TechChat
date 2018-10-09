from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet 


class CreateRetrieveUpdateDestroy(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Abstract ViewSet that provides endpoints for POST, GET, PUT, and DELETE requests.
    """

    @staticmethod
    def get_client_ip(request):
        """
        Returns:
            IPv4 or IPv6 address from which the HttpRequest originated.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
