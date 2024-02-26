import json
from django.http import HttpResponse, JsonResponse


from ..controller.EventController import EventController
from ..models.Event import Event

# from django.forms import 

eventController = EventController()
def index(request):
    return JsonResponse({"foo": "bar"})

def getEvent(request):
    events = eventController.getAll()
    return JsonResponse(events, safe=False)
    
def addEvent(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        event = Event()
        event.name = request_body['name']
        event.description = request_body['description']
        eventController.add(event)
        return JsonResponse(event.__dict__) 
    else: 
        return HttpResponse(status = 405)    