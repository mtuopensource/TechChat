from rest_framework_mongoengine import serializers
from .models import Board, Thread, User, Post, Participant
from django.utils.crypto import get_random_string

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
        read_only_fields = ('salt', 'hidden')
    def create(self, validated_data):
        salt = get_random_string(length=32)
        return User.objects.create(salt=salt, hidden=False, **validated_data)

class PostSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ParticipantSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
