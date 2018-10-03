from django.db.models import Model, CharField, SlugField


class Board(Model):
    """
    Represents a forum dedicated to a specific topic.

    Attributes:
        title: The Board's name. Limited to 32 characters. Must be unique.
        description: Short description of the Board's intended use. Limited to 128 characters.
        slug: Reserved for the web application. Limited to 32 characters. Must be unique.
    """

    title = CharField(max_length=32, unique=True)
    description = CharField(max_length=128)
    slug = SlugField(max_length=32, unique=True)

    def __str__(self):
        return self.title
