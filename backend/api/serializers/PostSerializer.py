from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault
from api.models.Post import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model   = Post
        exclude   = ('ip', )
        read_only_fields = ('id', 'author', 'ip', 'timestamp')