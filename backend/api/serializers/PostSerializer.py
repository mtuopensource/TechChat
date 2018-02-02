from rest_framework_mongoengine.serializers import DocumentSerializer
from api.models import Post, User
from api.utils import get_client_ip

class PostSerializer(DocumentSerializer):
    class Meta:
        model = Post
        fields = '__all__' # Fields stored in MongoDB
        read_only_fields = ('hidden', 'ip', 'author') # Fields computed automatically

    # Handles creating and saving a new Post instance.
    def create(self, validated_data):
        request = self.context.get('request')
        ip = get_client_ip(request)
        author = User.objects.get(id=request.session.get('techchat_userid')) # TODO Constants
        return Post.objects.create(ip=ip, author=author, **validated_data)
