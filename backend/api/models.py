from mongoengine import Document, EmbeddedDocument, fields
from mongoengine.queryset.base import DO_NOTHING

# http://docs.mongoengine.org/guide/defining-documents.html

class Board(Document):
    title = fields.StringField(max_length=32, required=True)
    description = fields.StringField(max_length=128, required=True, null=True)

class Thread(Document):
    board = fields.LazyReferenceField(Board)
    content = fields.StringField(max_length=512, required=True)

class User(Document):
    email = fields.EmailField(domain_whitelist = "mtu.edu", required = True)
    password = fields.StringField(required = True)
    #salt = fields.StringField(required = True)
    #hidden = fields.BooleanField(required = True, default = False)
