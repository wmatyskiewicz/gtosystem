# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from gtosystem.core.views.base import Base

class Home(Base):
    template_name = 'layout_2cols.html'
    page_title = 'Home'

    def sitebar(self):
        data = 'init data'
        return data

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context.update({
            'data': 'Hello content',
        })
        return context
