import datetime
from mongoengine import Document
from mongoengine.fields import BooleanField, DateTimeField, LazyReferenceField, StringField
from api.models.ThreadModel import Thread
from api.models.UserModel import User

class Post(Document):
    thread = LazyReferenceField(Thread, required=True)
    content = StringField(required = True)
    author = LazyReferenceField(User)
    date_created = DateTimeField()
    date_updated = DateTimeField()
    deleted = BooleanField(default = False)
    replyto = LazyReferenceField(User)

    # Need 39 characters to store an IPV6 address
    # ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
    # @see https://en.wikipedia.org/wiki/IPv6_address
    ip = StringField(max_length=39)

    # Automatically set the date_created field to now when the Post is first created.
    # Automatically set the date_updated field to now every time the Post is saved.
    def save(self, *args, **kwargs):
        if not self.date_created:
            self.date_created = datetime.datetime.now()
        self.date_updated = datetime.datetime.now()
        return super(Post, self).save(*args, **kwargs)
