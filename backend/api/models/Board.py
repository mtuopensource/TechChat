from django.db.models import Model, CharField, SlugField

class Board(Model):
    title       = CharField(max_length = 32, unique = True)
    description = CharField(max_length = 128)
    slug        = SlugField(max_length = 32, unique = True)

    def __str__(self):
        return self.title