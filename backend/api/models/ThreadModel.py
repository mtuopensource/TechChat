from mongoengine import Document
from mongoengine.fields import LazyReferenceField, StringField
from api.models.BoardModel import Board
from api.models.UserModel import User

class Thread(Document):
    board = LazyReferenceField(Board, required=True)
    content = StringField(required=True, max_length=512)
    author = LazyReferenceField(User)
    ip = StringField()
