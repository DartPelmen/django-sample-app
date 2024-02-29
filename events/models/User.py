from django.db import models
from django.contrib import admin


class User(models.Model):
    username = models.CharField(max_length = 150)
    password = models.TextField(default = "")
    events = models.ManyToManyField('Event')

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)    