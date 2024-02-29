from django.db import models
from django.contrib import admin

from .User import User

class Event(models.Model):
    eventName = models.CharField(max_length = 150)
    eventDescription = models.TextField(default = "")
    users = models.ManyToManyField(User, through=User.events.through)


class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
