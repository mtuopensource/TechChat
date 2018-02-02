from mongoengine import Document
from mongoengine.fields import BooleanField, LazyReferenceField, StringField
from api.models.ThreadModel import Thread
from api.models.UserModel import User

class Post(Document):
    # Specified by User
    thread = LazyReferenceField(Thread, required=True)
    content = StringField(required = True)
    replyto = LazyReferenceField(User)
    # Autofill
    author = LazyReferenceField(User)
    ip = StringField()
    hidden = BooleanField(Default = False)
