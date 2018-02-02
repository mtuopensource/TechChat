from mongoengine import Document
from mongoengine.fields import BooleanField, LazyReferenceField, StringField
from api.models.ThreadModel import Thread
from api.models.UserModel import User

class Post(Document):
    thread = LazyReferenceField(Thread, required=True)
    content = StringField(required = True)
    author = LazyReferenceField(User)
    deleted = BooleanField(Default = False)
    replyto = LazyReferenceField(User)

    # Need 39 characters to store an IPV6 address
    # ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
    # @see https://en.wikipedia.org/wiki/IPv6_address
    ip = StringField(max_length=39)
