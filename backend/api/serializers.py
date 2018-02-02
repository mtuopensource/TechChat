import bcrypt
from rest_framework_mongoengine import serializers
from api.models import Board, Thread, User, Post, Participant

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class BoardSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class ThreadSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Thread
        fields = '__all__'
        read_only_fields = ('author', 'ip')
    def create(self, validated_data):
        userid = self.context['request'].session.get('techchat_userid')
        author = User.objects.get(id=userid)
        ip = get_client_ip(self.context['request'])
        return Thread.objects.create(author=author, ip=ip, **validated_data)

class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('hidden', 'is_staff')
        write_only_fields = ('password',)

    def create(self, validated_data):
        password = validated_data.pop('password').encode('utf-8')
        hashedpw = bcrypt.hashpw(password, bcrypt.gensalt())
        return User.objects.create(password=hashedpw, hidden=False, **validated_data)

class PostSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('hidden', 'ip', 'author')
    def create(self, validated_data):
        userid = self.context['request'].session.get('techchat_userid')
        author = User.objects.get(id=userid)
        ip = get_client_ip(self.context['request'])
        return Post.objects.create(author=author, ip=ip, hidden=False, **validated_data)

class ParticipantSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
