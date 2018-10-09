from django.contrib.admin import register, ModelAdmin
from api.models import Board, Post, Comment

# Register Board, Post, and Comment with Django's CMS.
register(Board, Post, Comment)(ModelAdmin)
