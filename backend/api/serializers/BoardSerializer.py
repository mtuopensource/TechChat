from rest_framework_mongoengine.serializers import DocumentSerializer
from api.models import Board

class BoardSerializer(DocumentSerializer):
    class Meta:
        model = Board
        fields = '__all__' # Fields stored in MongoDB
