from api.models import Comment
from rest_framework.serializers import ModelSerializer


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('ip', )  # do not include ip address in response
        read_only_fields = ('id', 'author', 'ip', 'timestamp')  # cannot be updated by user
