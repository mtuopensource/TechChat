from rest_framework.permissions import BasePermission, SAFE_METHODS

# Authenticated have read access. Staff members have write access.
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        else:
            return request.user and request.user.is_staff

class TechChatIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.session.get('techchat_userid', False)
