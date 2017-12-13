from mongoengine import Document, EmbeddedDocument, fields
from mongoengine.queryset.base import DO_NOTHING

#http://docs.mongoengine.org/guide/defining-documents.html

class Board(Document):
    title = fields.StringField(max_length=32, required=True)
    description = fields.StringField(max_length=128, required=True, null=True)

class Thread(Document):
    board = fields.LazyReferenceField(Board)
    content = fields.StringField(max_length=512, required=True)

class User(Document):
    email = fields.EmailField(domain_whitelist = ("mtu.edu",), required = True)
    password = fields.StringField(required = True)
    salt = fields.StringField(required = True)
    hidden = fields.BooleanField(required = True, default = False)

class Post(Document):
    thread_id = fields.LazyReferenceField(Thread)
    user_id = fields.LazyReferenceField(User)
    text = fields.StringField(required = True)
    ip = fields.StringField(required = True)
    hidden = fields.BooleanField(required = True, Default = False)
    replyto_id = fields.LazyReferenceField(User)

class Participant(Document):
    user_id = fields.LazyReferenceField(User)
    thread_id = fields.LazyReferenceField(Thread)
    alias = fields.StringField(required = True)
