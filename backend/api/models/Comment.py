from api.models.Post import Post
from django.conf import settings
from django.db.models import Model, TextField, ForeignKey, GenericIPAddressField, DateTimeField, CASCADE


class Comment(Model):
    """
    Response to a Post.
    Consists of a user-submitted message containing the User's details and the date and time it was submitted.

    Attributes:
        description: User-submitted message. Limited to 512 characters.
        author: UUID of the Comments's author.
        ip: IPv4 or IPv6 address that originated the Comment. Normalized following RFC 4291.
        timestamp: The Comment's publication time. See RFC 3339.
        post: UUID of the Post replied to.
    """

    description = TextField(max_length=512)
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    ip = GenericIPAddressField()
    timestamp = DateTimeField(auto_now_add=True)
    post = ForeignKey(Post, on_delete=CASCADE)
    parent = ForeignKey('self', on_delete=CASCADE, blank=True, null=True)

    @property
    def owner(self):
        """
        Used to determine the User(s) allowed to update the Comment.
        See IsOwnerOrReadOnly permission class.

        Returns:
            Django User that authored the Comment.
        """
        return self.author
        
    def __str__(self):
        return self.content
