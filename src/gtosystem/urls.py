# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from gtosystem.core.views.home import Home

urlpatterns = patterns(
    '',
    url(r'^$', login_required(Home.as_view()), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
