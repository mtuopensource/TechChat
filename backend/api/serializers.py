import bcrypt
from rest_framework_mongoengine import serializers
from .models import Board, Thread, User, Post, Participant

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
        read_only_fields = ('hidden', 'is_staff')

    def create(self, validated_data):
        password = validated_data.pop('password').encode('utf-8')
        hashedpw = bcrypt.hashpw(password, bcrypt.gensalt())
        return User.objects.create(password=hashedpw, hidden=False, **validated_data)

class PostSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ParticipantSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
