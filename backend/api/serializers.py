from django.contrib.auth.models import User
from rest_framework import serializers as rest_serializers
from rest_framework_mongoengine import serializers
from .models import Board, Thread

class BoardSerializer(rest_serializers.DocumentSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class ThreadSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Thread
        fields = '__all__'
