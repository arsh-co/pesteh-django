# -*- coding: utf-8 -*-
from django import conf

PESTEH_URL = u"https://cloud.arsh.co/pesteh/"

REGISTER_DEVICE_URL = u"{}devices/register".format(PESTEH_URL)
SEND_MESSAGE_URL = u"{}send".format(PESTEH_URL)
EDIT_MESSAGE_URL = u"{}messages/edit".format(PESTEH_URL)

MAX_RETRIES = 50
PESTEH_SETTINGS = conf.settings.get('PESTEH_SETTINGS', {})
RETRY_SEND_REQUEST = PESTEH_SETTINGS.get('RETRY_SEND_REQUEST', True)
