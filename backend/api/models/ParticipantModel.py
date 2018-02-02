from mongoengine import Document
from mongoengine.fields import LazyReferenceField, StringField
from api.models.ThreadModel import Thread
from api.models.UserModel import User

class Participant(Document):
    user = LazyReferenceField(User)
    thread = LazyReferenceField(Thread)
    alias = StringField(required = True)
