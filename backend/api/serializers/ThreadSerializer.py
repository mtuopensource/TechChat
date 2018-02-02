from rest_framework_mongoengine.serializers import DocumentSerializer
from api.models import Thread, User
from api.utils import get_client_ip

class ThreadSerializer(DocumentSerializer):
    class Meta:
        model = Thread
        fields = '__all__' # Fields stored in MongoDB
        read_only_fields = ('deleted', 'ip', 'author') # Fields computed automatically

    # Handles creating and saving a new Thread instance.
    def create(self, validated_data):
        request = self.context.get('request')
        ip = get_client_ip(request)
        author = User.objects.get(id=request.session.get('techchat_userid')) # TODO Constants
        return Thread.objects.create(ip=ip, author=author, **validated_data)
