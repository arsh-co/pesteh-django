from django.conf import settings
from django.db import models


class PestehUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)
    user_token = models.CharField(max_length=63, unique=True)


class Device(models.Model):
    pesteh_user = models.ForeignKey(PestehUser, null=True, blank=True)
    token = models.CharField(max_length=127, unique=True)


class Message(models.Model):
    message_id = models.CharField(max_length=63, primary_key=True, editable=False)
    timestamp = models.DateTimeField()
    body = models.TextField()
    type = models.TextField(null=True, blank=True)
    user = models.ForeignKey(PestehUser, null=True)
    devices = models.ManyToManyField(Device)
