from rest_framework.serializers import ModelSerializer
from api.models.Comment import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model   = Comment
        exclude = ('timestamp', 'ip')