from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)


class Message(models.Model):
    room = models.ForeignKey(Room)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
