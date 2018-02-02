import bcrypt
from django.db.models import Manager
from mongoengine import Document
from mongoengine.fields import BooleanField, EmailField, StringField
from ..response import INSUFFICIENT_INFORMATION, INVALID_CREDENTIALS, SUCCESS

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
        from ..serializers import UserSerializer

        credentials = self.get_credentials_from_request(request)
        if not credentials:
            return INSUFFICIENT_INFORMATION.as_response()

        user = User.objects.get(email=credentials.get('username'))
        if user.check_password(credentials.get('password')):
            response = SUCCESS.as_response()
            request.session['techchat_userid'] = str(user.id)
            request.session.modified = True
            return response
        else:
            return INVALID_CREDENTIALS.as_response()

class User(Document):
    email    = EmailField(unique=True, required=True, max_length=254)
    password = StringField(required=True)
    deleted   = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    login_manager = LoginManager()
    def check_password(self, password):
        a = password.encode('utf-8')
        b = self.password.encode('utf-8')
        return bcrypt.checkpw(a, b)
