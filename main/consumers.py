from channels import Group
from channels.sessions import channel_session
import json

from .models import Room


@channel_session
def ws_connect(message):
    prefix, label = message['path'].strip('/').split('/')
    room = Room.objects.get(name=label)
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = room.name


@channel_session
def ws_recieve(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    data = json.loads(message['text'])
    m = room.room.create(message=data['message'])
    Group('chat-' + label).send({'text': json.dumps(m.as_dict())})


@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-' + label).discard(message.reply_channel)
