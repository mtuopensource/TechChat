from mongoengine import Document
from mongoengine.fields import StringField

class Board(Document):
    title = StringField(unique=True, required=True, max_length=32)
    description = StringField(required=True, null=True, max_length=128)
