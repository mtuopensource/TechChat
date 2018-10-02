from django.conf import settings
from django.db.models import Model, CharField, ForeignKey, CASCADE, TextField, DateTimeField, GenericIPAddressField
from api.models.Board import Board

class Post(Model):
    board     = ForeignKey(Board, on_delete = CASCADE)
    title     = CharField(max_length = 32)
    content   = TextField(max_length = 512)
    timestamp = DateTimeField(auto_now_add = True)
    ip        = GenericIPAddressField()
    # TODO author

    def __str__(self):
        return self.title