from django.db.models import Manager
from mongoengine import DoesNotExist
from api.response import INSUFFICIENT_INFORMATION, INVALID_CREDENTIALS, SUCCESS

class LoginManager(Manager):

    # Returns 200 OK           if the credentials were correct
    # Returns 401 UNAUTHORIZED if the credentials were invalid
    # Returns 400 BAD REQUEST  if the credentials were not provided
    # @see https://docs.djangoproject.com/en/2.0/topics/http/sessions/
    def login(self, request):
        username = self.get_username_from_request(request)
        password = self.get_password_from_request(request)
        if not username or not password:
            return INSUFFICIENT_INFORMATION.as_response() # Email or password was not provided
        else:
            try:
                from api.models import User # XXX Circular dependencies
                user = User.objects.get(email=username)
                if user.check_password(password):
                    response = SUCCESS.as_response() # User exists and the password matches, we're in
                    request.session['techchat_userid'] = str(user.id) # TODO Constants
                    request.session.modified = True # Save changes to the database
                    return response
                else:
                    return INVALID_CREDENTIALS.as_response() # User exists, but the password does not match
            except DoesNotExist:
                    return INVALID_CREDENTIALS.as_response() # User does not exist

    # Ends any existing sessions.
    # Returns 200 OK
    # @see https://docs.djangoproject.com/en/2.0/topics/http/sessions/
    def logout(self, request):
        if 'techchat_userid' in request.session:
            del request.session['techchat_userid'] # TODO Constants
            request.session.modified = True # Save changes to the database
        return SUCCESS.as_response()

    def get_username_from_request(self, request):
        username = None
        if 'email' in request.GET:
            username = request.GET.get('email')
        elif 'email' in request.data:
            username = request.data.get('email')
        return username

    def get_password_from_request(self, request):
        password = None
        if 'password' in request.GET:
            password = request.GET.get('password')
        elif 'password' in request.data:
            password = request.data.get('password')
        return password
