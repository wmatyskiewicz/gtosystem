from django.views.generic import TemplateView
from gtosystem import VERSION

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
            {'version': '%s' % '.'.join((str(part) for part in VERSION))}
        ]
        context.update({
            'mainmenu_items': mainmenu_items,
            'sitebar': self.sitebar(),
            'page_title': self.page_title,
            'footer_items': footer_items,
        })
        return context
