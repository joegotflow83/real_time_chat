from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import Room


class CreateRoom(CreateView):
    """Users can create chat rooms"""
    model = Room
    fields = ('name')

    def get_success_url(self):
        room = Room.objects.first()
        return reverse('chat_room', kwargs={'room': room.name})


class ChatRoom(ListView):
    """Chat room users can send messages"""


class Chat(ListView):
    """Page where users can chat"""
    model = Room
