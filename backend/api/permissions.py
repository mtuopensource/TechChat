from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models import User

class TechChatIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return 'techchat_userid' in request.session

class TechChatIsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if 'techchat_userid' in request.session:
            if request.method in SAFE_METHODS:
                return True
            else:
                userid = request.session.get('techchat_userid')
                user   = User.objects.get(id=userid)
                return user.is_staff
        else:
            return False

class TechChatIsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return 'techchat_userid' in request.session
    def has_object_permission(self, request, view, obj):
        if 'techchat_userid' in request.session:
            if request.method in SAFE_METHODS:
                return True
            else:
                userid = request.session.get('techchat_userid')
                user   = User.objects.get(id=userid)
                return user.is_staff or user.id == obj.author.id
        else:
            return False
