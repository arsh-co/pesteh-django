# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'pesteh.views',
    url(r'^register-device/$', 'register_pesteh_device', name='pesteh/register-device'),
)
