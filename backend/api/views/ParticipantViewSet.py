from rest_framework.viewsets import ModelViewSet
from api.models import Participant
from api.serializers import ParticipantSerializer
from api.permissions import TechChatIsAdminOrReadOnly

# Participants can be listed, created, retrieved, updated, and destroyed.
class ParticipantViewSet(ModelViewSet):
    permission_classes = (TechChatIsAdminOrReadOnly,) # Only allow admins to create, update, destroy
    serializer_class = ParticipantSerializer
    lookup_field = 'id'

    #Set of all Participants
    def get_queryset(self):
        return Participant.objects.all()
