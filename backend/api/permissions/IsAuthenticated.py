from rest_framework.permissions import BasePermission

# Grants full permissions if the User is authenticated.
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return 'techchat_userid' in request.session # TODO Constants
