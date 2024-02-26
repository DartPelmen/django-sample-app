from django.db import models
from django.contrib import admin

class User(models.Model):
    username = models.CharField(max_length = 150)
    password = models.TextField(default = "")
    events = models.ManyToManyField('Event')

class Event(models.Model):
    eventName = models.CharField(max_length = 150)
    eventDescription = models.TextField(default = "")
    users = models.ManyToManyField(User, through=User.events.through)



class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
