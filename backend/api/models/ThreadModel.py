from mongoengine import Document
from mongoengine.fields import BooleanField, LazyReferenceField, StringField
from api.models.BoardModel import Board
from api.models.UserModel import User

class Thread(Document):
    board = LazyReferenceField(Board, required=True)
    content = StringField(required=True, max_length=512)
    author = LazyReferenceField(User)
    deleted = BooleanField(Default = False)

    # Need 39 characters to store an IPV6 address
    # ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
    # @see https://en.wikipedia.org/wiki/IPv6_address
    ip = StringField(max_length=39)
