from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models import User
from api.resources import Constants

class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return Constants.USER_ID_KEY in request.session # XXX Prevents the has_object_permission function from short circuiting

    def has_object_permission(self, request, view, obj):
        if Constants.USER_ID_KEY in request.session:
            if request.method in SAFE_METHODS:
                return True # User is authenticated, grant read permissions
            else:
                user   = User.objects.get(id=request.session.get(Constants.USER_ID_KEY))
                return user.is_staff or user.id == obj.author.id # User is an administrator, grant full permissions
        else:
            return False # User is not authenticated, no permissions
