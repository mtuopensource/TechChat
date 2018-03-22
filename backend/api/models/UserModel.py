import bcrypt
import os
import datetime
from mongoengine import Document
from mongoengine.fields import BooleanField, DateTimeField, EmailField, StringField
from api.managers import LoginManager

class User(Document):
    # The RFC5321 standard caps the maximum length of an email address at 254 characters.
    # @see https://tools.ietf.org/html/rfc5321
    email = EmailField(unique=True, required=True, max_length=254)
    password = StringField(required=True)
    date_created = DateTimeField()
    date_updated = DateTimeField()
    deleted = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    # Automatically set the date_created field to now when the User is first created.
    # Automatically set the date_updated field to now every time the User is saved.
    def save(self, *args, **kwargs):
        if not self.date_created:
            self.date_created = datetime.datetime.now()
        self.date_updated = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)

    login_manager = LoginManager()
    def check_password(self, password):
        a = password.encode(os.getenv('ENCODING'))
        b = self.password.encode(os.getenv('ENCODING'))
        return bcrypt.checkpw(a, b)
