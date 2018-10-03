from django.contrib.admin import register, ModelAdmin
from api.models import Board, Post, Comment

register(Board, Post, Comment)(ModelAdmin)
