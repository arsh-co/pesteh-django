# -*- coding: utf-8 -*-

from django.conf import settings


def send_request(url, data, use_client_id=True, use_client_secret=True):
    import json
    import httplib2

    if use_client_id:
        data.update({'client_id': settings.PESTEH_CLIENT_ID})
    if use_client_secret:
        data.update({'client_secret': settings.PESTEH_CLIENT_SECRET})
    params = json.dumps(data)
    h = httplib2.Http()
    resp, content = h.request(url, body=params, method="POST", headers={u"content-type": 'application/json'})
    return json.loads(content)


def generate_user_token(user):
    if not user.is_authenticated():
        return None
    return u"PESTEH-ut-P{}".format(user.id)
