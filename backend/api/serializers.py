from rest_framework_mongoengine import serializers
from .models import Board

class BoardSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Board
        fields = '__all__'
