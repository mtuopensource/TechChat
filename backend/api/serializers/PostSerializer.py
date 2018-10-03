from api.models import Post
from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ('ip', )  # do not include ip address in response
        read_only_fields = ('id', 'author', 'ip', 'timestamp')  # cannot be updated by user
