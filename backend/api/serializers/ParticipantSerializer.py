from rest_framework_mongoengine.serializers import DocumentSerializer
from api.models import Participant

class ParticipantSerializer(DocumentSerializer):
    class Meta:
        model = Participant
        fields = '__all__' # Fields stored in MongoDB
