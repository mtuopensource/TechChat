from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'date_joined')
        read_only_fields = ('id', 'date_joined')  # cannot be updated by user
        extra_kwargs = {
            'password': {
                'write_only': True,  # do not include in response
            },
            'email': {
                'write_only': True,  # do not include in response
                'required': True  # require an email address to create an account
            }
        }

    def create(self, validated_data):
        """
        Create and save a User with the given email and password.
        Parameters:
            validated_data: HttpRequest that has been validated and sanitized.
        Returns:
            Django User
        """
        email_address = validated_data['email']
        password = validated_data['password']
        return User.objects.create_user(email_address, email_address, password)
