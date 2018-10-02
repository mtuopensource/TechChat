from django.contrib.admin import site
from api.models.Board import Board
from api.models.Post import Post
from api.models.Comment import Comment

site.register(Board)
site.register(Post)
site.register(Comment)