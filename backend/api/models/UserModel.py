import bcrypt
from mongoengine import Document
from mongoengine.fields import BooleanField, EmailField, StringField
from api.managers import LoginManager

class User(Document):
    # The RFC5321 standard caps the maximum length of an email address at 254 characters.
    # @see https://tools.ietf.org/html/rfc5321
    email = EmailField(unique=True, required=True, max_length=254)
    password = StringField(required=True)
    deleted = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    login_manager = LoginManager()
    def check_password(self, password):
        a = password.encode('utf-8') # TODO Environment variables
        b = self.password.encode('utf-8') # TODO Environment variables
        return bcrypt.checkpw(a, b)
