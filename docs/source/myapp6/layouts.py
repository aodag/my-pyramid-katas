from pyramid_layout.layout import layout_config


@layout_config(template="templates/base.jinja2")
class BaseLayout(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request
