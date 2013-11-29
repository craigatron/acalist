from django.shortcuts import render
from models import Event

from django.template import RequestContext
from django.views.decorators.http import require_GET

@require_GET
def events_list(request):
  event_list = Event.objects.all()
  return render(request, 'events/event_list.html',
      dictionary={'events': event_list},
      context_instance=RequestContext(request))
