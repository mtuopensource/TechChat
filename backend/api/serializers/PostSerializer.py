import humanize
import datetime
from rest_framework.serializers import SerializerMethodField
from rest_framework_mongoengine.serializers import DocumentSerializer
from api.models import Post, User
from api.utils import get_client_ip
from api.serializers.UserSerializer import UserSerializer

class PostSerializer(DocumentSerializer):
    author_friendly = SerializerMethodField()
    date_created_friendly = SerializerMethodField()
    date_updated_friendly = SerializerMethodField()

    class Meta:
        model = Post
        exclude = ('ip',) # Fields not displayed publicly
        read_only_fields = ('author', 'date_created', 'date_updated', 'deleted') # Fields computed automatically

    # Handles creating and saving a new Post instance.
    def create(self, validated_data):
        request = self.context.get('request')
        ip = get_client_ip(request)
        author = User.objects.get(id=request.session.get('techchat_userid')) # TODO Constants
        return Post.objects.create(ip=ip, author=author, **validated_data)

    def get_date_created_friendly(self, post):
        return humanize.naturaltime(datetime.datetime.now() - post.date_created)

    def get_date_updated_friendly(self, post):
        return humanize.naturaltime(datetime.datetime.now() - post.date_updated)

    def get_author_friendly(self, post):
        serializer = UserSerializer(User.objects.get(id=post.author.id))
        return serializer.data
