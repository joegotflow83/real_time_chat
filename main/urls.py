from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^$', views.Chat.as_view(), name='chat'),
    url(r'^room/create/$', views.CreateRoom.as_view(), name='create_room'),
    url(r'^room/(?P<room>\w+)/$', views.ChatRoom.as_view(), name='chat_room')
]
