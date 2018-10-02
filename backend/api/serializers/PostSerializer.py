from rest_framework.serializers import ModelSerializer
from api.models.Post import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model   = Post
        exclude = ('timestamp', 'ip')