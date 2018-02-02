from mongoengine import Document
from mongoengine.fields import LazyReferenceField, StringField
from api.models.BoardModel import Board

class Thread(Document):
    board = LazyReferenceField(Board)
    content = StringField(required=True, max_length=512)
