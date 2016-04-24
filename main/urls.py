from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^$', views.Chat.as_view(), name='chat'),
]
