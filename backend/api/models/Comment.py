from django.conf import settings
from django.db.models import Model, ForeignKey, CASCADE, TextField, DateTimeField, GenericIPAddressField
from api.models.Post import Post

class Comment(Model):
    author    = ForeignKey(settings.AUTH_USER_MODEL, on_delete = CASCADE)
    ip        = GenericIPAddressField()
    timestamp = DateTimeField(auto_now_add = True)
    post      = ForeignKey(Post, on_delete = CASCADE)
    parent    = ForeignKey('self', on_delete = CASCADE, blank = True, null = True)
    content   = TextField(max_length = 512)
    
    @property
    def owner(self):
        return self.author
        
    def __str__(self):
        return self.content