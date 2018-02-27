import bcrypt
from rest_framework_mongoengine.serializers import DocumentSerializer
from api.models import User

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__' # Fields stored in MongoDB
        read_only_fields = ('date_created', 'date_updated', 'deleted', 'is_staff') # Fields computed automatically
        extra_kwargs = {
            'password': {
                'write_only': True # Never displayed publicly
            }
        }

    # Handles creating and saving a new User instance.
    def create(self, validated_data):
        password = validated_data.pop('password').encode('utf-8') # TODO Environment variables
        return User.objects.create(password=bcrypt.hashpw(password, bcrypt.gensalt()), **validated_data)
