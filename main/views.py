from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import Room, Message


class CreateRoom(CreateView):
    """Users can create chat rooms"""
    model = Room
    fields = ('name',)

    def get_success_url(self):
        room = Room.objects.first()
        return reverse('chat_room', kwargs={'room': room.name, 'pk': room.pk})


class ChatRoom(TemplateView):
    """Chat room users can send messages"""
    template_name = 'main/chatroom.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(room=self.kwargs['pk'])[:50]
        context['room'] = Room.objects.get(name=self.kwargs['room'])
        return context


class Rooms(ListView):
    """Page where users can chat"""
    model = Room
