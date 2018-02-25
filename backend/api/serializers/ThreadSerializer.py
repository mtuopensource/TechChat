import humanize
import datetime
from rest_framework.serializers import SerializerMethodField
from rest_framework_mongoengine.serializers import DocumentSerializer
from api.models import Thread, User
from api.utils import get_client_ip

class ThreadSerializer(DocumentSerializer):
    date_created_friendly = SerializerMethodField()
    date_updated_friendly = SerializerMethodField()

    class Meta:
        model = Thread
        exclude = ('ip',) # Fields not displayed publicly
        read_only_fields = ('author', 'date_created', 'date_updated', 'deleted') # Fields computed automatically

    # Handles creating and saving a new Thread instance.
    def create(self, validated_data):
        request = self.context.get('request')
        ip = get_client_ip(request)
        author = User.objects.get(id=request.session.get('techchat_userid')) # TODO Constants
        return Thread.objects.create(ip=ip, author=author, **validated_data)

    def get_date_created_friendly(self, user):
        return humanize.naturaltime(datetime.datetime.now() - user.date_created)

    def get_date_updated_friendly(self, user):
        return humanize.naturaltime(datetime.datetime.now() - user.date_updated)
