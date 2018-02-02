from mongoengine import Document
from mongoengine.fields import BooleanField, LazyReferenceField, StringField
from api.models.ThreadModel import Thread
from api.models.UserModel import User

class Post(Document):
    content = StringField(required = True)
    thread = LazyReferenceField(Thread, required=True)
    replyto = LazyReferenceField(User)
    author = LazyReferenceField(User)
    ip = StringField(max_length=39)
    hidden = BooleanField(Default = False)
