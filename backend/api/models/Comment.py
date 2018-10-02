from django.conf import settings
from django.db.models import Model, ForeignKey, CASCADE, TextField, DateTimeField, GenericIPAddressField
from api.models.Post import Post

class Comment(Model):
    post      = ForeignKey(Post, on_delete = CASCADE)
    content   = TextField(max_length = 512)
    parent    = ForeignKey('self', on_delete = CASCADE, blank = True, null = True)
    timestamp = DateTimeField(auto_now_add = True)
    ip        = GenericIPAddressField()
    # TODO author

    def __str__(self):
        return self.content