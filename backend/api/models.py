from django.db import models
import mongoengine # this is to make sure you have mongo engine

class Board(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
