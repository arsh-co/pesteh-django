import json

from dateutil.parser import parse
from django.conf import settings
from django.http import HttpResponse

from consts import SEND_MESSAGE_URL, REGISTER_DEVICE_URL
from models import Device
from pesteh import send_request, generate_user_token


def register_pesteh_device(request):
    data = {u"user_id": generate_user_token(request.user)}
    result = send_request(REGISTER_DEVICE_URL, data)
    Device.objects.create(token=result.get(u"token"))
    return HttpResponse(json.dumps(result), content_type=u'application/json')


def send_pesteh_message(message):
    data = {
        u'type': message.type,
        u'message': message.body,
    }
    if message.user:
        data[u"user_id"] = generate_user_token(message.user)
    elif message.devices.exists():
        devices_id = []
        for d in message.devices.all():
            devices_id.append(d.token)
        data[u"device_id"] = devices_id
    result = send_request(SEND_MESSAGE_URL, data)
    message_obj = result.get(u"message")
    if not settings.USE_TZ:
        date = parse(message_obj[u"timestamp"])
        date = date.replace(tzinfo=None)
        message_obj[u"timestamp"] = date
    message.timestamp = message_obj.get('timestamp')
    message.message_id = message_obj.get('message_id')
    message.save()
    return {u"result": u"success"}
