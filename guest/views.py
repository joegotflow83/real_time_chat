from django.views.generic import TemplateView


class Index(TemplateView):
    """Landing Page"""
    template_name = 'guest/index.html'
