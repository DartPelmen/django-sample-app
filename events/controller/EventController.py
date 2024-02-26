

from ..models.Event import Event
from ..services.EventService import EventService


class EventController:
    def __init__(self):
        self.eventService = EventService()
    def add(self, event: Event):
        self.eventService.addEvent(event)
    def getAll(self):
        return self.eventService.getEvents()
