import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "real_chat.settings")
channel_layer = channels.asgi.get_channel_layer()
