import json
from django.http import HttpResponse, JsonResponse


from ..controller.EventController import EventController
from .EventModel import EventModel
from ..models.Event import Event

eventController = EventController()
def index(request):
    return JsonResponse({"foo": "bar"})

def getEvent(request):
    events = eventController.getAll()
    return JsonResponse(events, safe=False)
    
def addEvent(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        eventModel = EventModel()
        eventModel.eventName = request_body['name']
        eventModel.eventDescription = request_body['description']
        event = Event(eventName = eventModel.eventName, eventDescription = eventModel.eventDescription)
        eventController.add(event)
        return JsonResponse(eventModel.__dict__) 
    else: 
        return HttpResponse(status = 405)    

def deleteEvent(request):
    if request.method == 'DELETE':
         request_body = json.loads(request.body)
         id = request_body['eventId']
         eventController.deleteById(id)
         return HttpResponse(status = 200) 