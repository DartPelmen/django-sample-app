import json
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


from ..controller.EventController import EventController
from .EventModel import EventModel
from ..models.Event import Event

eventController = EventController()
def index(request):
    return JsonResponse({"foo": "bar"})

@login_required
def getEvent(request):
    events = eventController.getAll()
    #здесь нужна конвертация в EventModel
    return JsonResponse(events, safe=False)
    

def addEvent(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        eventModel = EventModel()
        eventModel.eventName = request_body['name']
        eventModel.eventDescription = request_body['description']
        eventController.add(Event(eventName = eventModel
                                  .eventName,
                                  eventDescription = eventModel
                                  .eventDescription))
        return JsonResponse(eventModel.__dict__) 
    else: 
        return HttpResponse(status = 405)    

def deleteEvent(request):
    if request.method == 'DELETE':
         request_body = json.loads(request.body)
         id = request_body['eventId']
         eventController.deleteById(id)
         return HttpResponse(status = 200) 
    

# def user_login(request):
#     if request.method == 'POST':
#         form = request.AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})