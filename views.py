from dateutil.parser import parse
from django.conf import settings

from django.db import IntegrityError

from consts import REGISTER_USER_URL, SEND_MESSAGE_URL, REGISTER_DEVICE_URL
from models import PestehUser, Device, Message
from pesteh import send_request


def register_pesteh_device(user):
    try:
        pesteh_user = PestehUser.objects.get(user=user)
    except IntegrityError:
        result, pesteh_user = register_pesteh_user(user)
    data = {
        u"user_id": pesteh_user.user_token,
    }
    result = send_request(REGISTER_DEVICE_URL, data)
    device = Device.objects.create(pesteh_user=pesteh_user,
                                   token=result.get(u"token"))
    return result, device


def register_pesteh_user(user):
    try:
        pesteh_user = PestehUser.objects.get(user=user)
        return {u"result": u"success"}, pesteh_user
    except PestehUser.DoesNotExist:
        pesteh_user = PestehUser.objects.create(user=user)
    data = {
        u"user_id": pesteh_user.user_token
    }
    result = send_request(REGISTER_USER_URL, data)
    return result, pesteh_user


def send_pesteh_message(user=None, devices=None, message_type=u"", message_body=u""):
    data = {
        u'type': message_type,
        u'message': message_body,
    }
    if user:
        try:
            pesteh_user = PestehUser.objects.get(user=user)
        except PestehUser.DoesNotExist:
            r, pesteh_user = register_pesteh_user(user)
        data.update({
            u"user_id": pesteh_user.user_token
        })
    elif devices:
        devices_id = []
        for device in devices:
            devices_id.append(device.token)
        data.update({u"device_id": devices_id})
    result = send_request(SEND_MESSAGE_URL, data)
    message_obj = result.get(u"message")
    if not settings.USE_TZ:
        date = parse(message_obj[u"timestamp"])
        date = date.replace(tzinfo=None)
        message_obj[u"timestamp"] = date
    message = Message.objects.create(**message_obj)
    if user:
        message.user = pesteh_user
        message.save()
    else:
        for device in devices:
            message.devices.add(device)
        message.save()
    return {u"result": u"success"}, message
