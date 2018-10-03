from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, instance):
        """
        Determines if the User(s) have permission to perform a destructive action.
        User(s) considered an 'owner' of an object are given this permission.

        Parameters:
            request: HttpRequest containing the method and user.
            view: Unused.
            instance: Object with an 'owner' attribute.

        Returns:
            True if the User(s) have permission. False otherwise.
        """
        if not hasattr(instance, 'owner'):
            raise ValueError()
        if request.method in SAFE_METHODS:
            return True
        return instance.owner == request.user
