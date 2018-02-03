import datetime
from mongoengine import Document
from mongoengine.fields import BooleanField, DateTimeField, LazyReferenceField, StringField
from api.models.BoardModel import Board
from api.models.UserModel import User

class Thread(Document):
    board = LazyReferenceField(Board, required=True)
    content = StringField(required=True, max_length=512)
    author = LazyReferenceField(User)
    date_created = DateTimeField()
    date_updated = DateTimeField()
    deleted = BooleanField(default=False)

    # Need 39 characters to store an IPV6 address
    # ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
    # @see https://en.wikipedia.org/wiki/IPv6_address
    ip = StringField(max_length=39)

    # Automatically set the date_created field to now when the Thread is first created.
    # Automatically set the date_updated field to now every time the Thread is saved.
    def save(self, *args, **kwargs):
        if not self.date_created:
            self.date_created = datetime.datetime.now()
        self.date_updated = datetime.datetime.now()
        return super(Thread, self).save(*args, **kwargs)
