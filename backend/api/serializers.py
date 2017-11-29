from django.contrib.auth.models import User
from rest_framework_mongoengine import serializers
from .models import Board, Thread, User

class BoardSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class ThreadSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'
