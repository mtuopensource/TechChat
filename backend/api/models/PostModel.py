from mongoengine import Document
from mongoengine.fields import BooleanField, LazyReferenceField, StringField
from api.models.ThreadModel import Thread
from api.models.UserModel import User

class Post(Document):
    thread = LazyReferenceField(Thread)
    user = LazyReferenceField(User)
    text = StringField(required = True)
    ip = StringField()
    hidden = BooleanField(Default = False)
    replyto_id = LazyReferenceField(User)
