from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models import User
from api.resources import Constants

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if Constants.USER_ID_KEY in request.session:
            if request.method in SAFE_METHODS:
                return True # User is authenticated, grant read permissions
            else:
                user = User.objects.get(id=request.session.get(Constants.USER_ID_KEY))
                return user.is_staff # User is an administrator, grant full permissions
        else:
            return False # User is not authenticated, no permissions
