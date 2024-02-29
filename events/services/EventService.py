from ..models.Event import Event

class EventService:
    def __init__(self):
        self.__events__ = []
    
    def getEvents(self):
        return list(Event.objects.all().values())
    
    def addEvent(self, event: Event):
        Event.save(event)

    def dropEventById(self, id: int):
        #Здесь нужна проверка наличия Event по ID
        Event.objects.get(pk = id).delete()