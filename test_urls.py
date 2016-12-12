# encoding: utf-8
# Created by Jeremy Bowman on Fri Feb 21 14:28:40 EST 2014
# Copyright (c) 2014, 2015 Safari Books Online. All rights reserved.
#
# This software may be modified and distributed under the terms
# of the 3-clause BSD license.  See the LICENSE file for details.
"""
URL configuration for Yet Another Django Profiler tests.
"""

import django
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse, StreamingHttpResponse
from django.views.generic.base import View


class TestView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('This is only a test.')


class StreamingView(View):

    def get(self, request, *args, **kwargs):
        return StreamingHttpResponse(('Line {}\n'.format(i + 1) for i in range(100)))


if django.VERSION[0] == 1 and django.VERSION[1] < 7:
    admin.autodiscover()

urlpatterns = [
    url(r'^test/$', TestView.as_view(), name='test'),
    url(r'^test/streaming/$', StreamingView.as_view(), name='test_streaming'),
    url(r'^admin/', include(admin.site.urls)),
]
