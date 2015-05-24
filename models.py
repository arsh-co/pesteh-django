import json

import datetime
from django.conf import settings
from django.db import models


class Device(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    token = models.CharField(max_length=127, unique=True)
    # TODO: add extra information about device


class Message(models.Model):
    message_id = models.CharField(max_length=63, null=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    body = models.TextField()
    type = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    devices = models.ManyToManyField(Device)

    def remove(self):
        pass

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.body = json.dumps(self.body)
        except ValueError and TypeError:
            pass
        super(Message, self).save()
