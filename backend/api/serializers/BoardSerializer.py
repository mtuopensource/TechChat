from api.models import Board
from rest_framework.serializers import ModelSerializer


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
