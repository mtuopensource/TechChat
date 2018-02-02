import bcrypt
from mongoengine import Document, EmbeddedDocument, fields
from mongoengine.queryset.base import DO_NOTHING
from django.db.models import Manager
from .response import INSUFFICIENT_INFORMATION, INVALID_CREDENTIALS, SUCCESS

class LoginManager(Manager):
    def get_credentials_from_request(self, request):
        credentials = {}
        # Location of the username and password might be in the parameters or body
        if 'email' in request.data and 'password' in request.data: # Check if the username and password was provided
            credentials.update(username = request.data.get('email'))
            credentials.update(password = request.data.get('password'))
        elif 'email' in request.GET and 'password' in request.GET: # Check if the username and password was provided
            credentials.update(username = request.GET.get('email'))
            credentials.update(password = request.GET.get('password'))
        return credentials

    def login(self, request):
        from .serializers import UserSerializer

        credentials = self.get_credentials_from_request(request)
        if not credentials:
            return INSUFFICIENT_INFORMATION.as_response()

        users = User.objects.all()
        ids = [user.id for user in users if user.login(credentials.get('username'), credentials.get('password'))]
        queryset = users.filter(id__in=ids) # Set of User objects with the given email and password
        serializer = UserSerializer(queryset, context={'request': request}, many=True)

        # Does not exist
        if not serializer.data:
            return INVALID_CREDENTIALS.as_response()
        else:
            return SUCCESS.as_response()

# http://docs.mongoengine.org/guide/defining-documents.html

class Board(Document):
    title = fields.StringField(max_length=32, required=True)
    description = fields.StringField(max_length=128, required=True, null=True)

class Thread(Document):
    board = fields.LazyReferenceField(Board)
    content = fields.StringField(max_length=512, required=True)

class User(Document):
    email = fields.EmailField(domain_whitelist = ("mtu.edu",), required = True)
    password = fields.StringField(required = True)
    hidden = fields.BooleanField(required = True, default = False)

    login_manager = LoginManager()
    def login(self, email, password):
        a =      password.encode('utf-8')
        b = self.password.encode('utf-8')
        return bcrypt.checkpw(a, b) and self.email == email

class Post(Document):
    thread_id = fields.LazyReferenceField(Thread)
    user_id = fields.LazyReferenceField(User)
    text = fields.StringField(required = True)
    ip = fields.StringField(required = True)
    hidden = fields.BooleanField(required = True, Default = False)
    replyto_id = fields.LazyReferenceField(User)

class Participant(Document):
    user_id = fields.LazyReferenceField(User)
    thread_id = fields.LazyReferenceField(Thread)
    alias = fields.StringField(required = True)
