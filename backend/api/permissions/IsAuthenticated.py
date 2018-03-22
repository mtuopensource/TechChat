from rest_framework.permissions import BasePermission
from api.resources import Constants

# Grants full permissions if the User is authenticated.
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return Constants.USER_ID_KEY in request.session
