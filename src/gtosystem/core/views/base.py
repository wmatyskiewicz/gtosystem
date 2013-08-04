# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.views.generic import TemplateView

from gtosystem import get_version

class Base(TemplateView):
    page_title = None

    def sitebar(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(Base, self).get_context_data(**kwargs)
        mainmenu_items = [
            {'url': '/', 'link_name': 'home'}
        ]
        footer_items = [
            {'version': get_version()}
        ]
        context.update({
            'mainmenu_items': mainmenu_items,
            'sitebar': self.sitebar(),
            'page_title': self.page_title,
            'footer_items': footer_items,
        })
        return context
