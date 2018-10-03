from django.conf import settings
from django.db.models import Model, CharField, ForeignKey, CASCADE, TextField, DateTimeField, GenericIPAddressField
from api.models.Board import Board


class Post(Model):
    """
    Consists of a user-submitted message containing the User's details and the date and time it was submitted.

    Attributes:
        title: The Post's title. Limited to 32 characters.
        description: Summary of the intended discussion. Limited to 512 characters.
        author: UUID of the Post's author.
        ip: IPv4 or IPv6 address that originated the Post. Normalized following RFC 4291.
        timestamp: The Post's publication time. See RFC 3339.
        board: UUID of the Post's discussion Board.
    """

    title = CharField(max_length=32)
    description = TextField(max_length=512)
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    ip = GenericIPAddressField()
    timestamp = DateTimeField(auto_now_add=True)
    board = ForeignKey(Board, on_delete=CASCADE)

    @property
    def owner(self):
        """
        Used to determine the User(s) allowed to update the Post.
        See IsOwnerOrReadOnly permission class.

        Returns:
            Django User that authored the Post.
        """
        return self.author

    def __str__(self):
        return self.title
