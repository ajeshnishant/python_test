from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    duration_in_seconds = models.PositiveIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration_in_seconds = models.PositiveIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = ArrayField(models.CharField(max_length=100), blank=True, size=10)

class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration_in_seconds = models.PositiveIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)



