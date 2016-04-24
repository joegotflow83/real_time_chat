from django.views.generic import TemplateView


class Chat(TemplateView):
    """Page where users can chat"""
    template_name = 'chat/chat.html'
