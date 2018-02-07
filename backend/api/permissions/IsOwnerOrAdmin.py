from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models import User

class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return 'techchat_userid' in request.session # XXX Prevents the has_object_permission function from short circuiting

    def has_object_permission(self, request, view, obj):
        if 'techchat_userid' in request.session:
            if request.method in SAFE_METHODS:
                return True # User is authenticated, grant read permissions
            else:
                user   = User.objects.get(id=request.session.get('techchat_userid')) # TODO Constants
                return user.is_staff or user.id == obj.author.id # User is an administrator, grant full permissions
        else:
            return False # User is not authenticated, no permissions
