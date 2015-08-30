# -*- coding: utf-8 -*-

from django.conf import settings
import requests
from requests.packages.urllib3.connection import ConnectionError
import time


def send_request(url, data, use_client_id=True, use_client_secret=True):
    import json

    if use_client_id:
        data.update({'client_id': settings.PESTEH_CLIENT_ID})
    if use_client_secret:
        data.update({'client_secret': settings.PESTEH_CLIENT_SECRET})
    params = json.dumps(data)

    c = 0
    while c < 100:
        c += 1
        try:
            resp = requests.post(url, data=params, headers={u"content-type": 'application/json'})
        except ConnectionError:
            time.sleep(0.05)
        else:
            break
    return json.loads(resp.content)


def generate_user_token(user):
    if not user.is_authenticated():
        return None
    return u"PESTEH-ut-P{}".format(user.id)
