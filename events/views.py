import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.http import require_GET
from models import Event


@require_GET
def events_list(request):
  event_list = Event.objects.all()
  return render(request, 'events/event_list.html',
      dictionary={'events': event_list},
      context_instance=RequestContext(request))

@require_GET
def event_locations(request):
  date = datetime.datetime.now().date()
  event_list = Event.objects.exclude(latitude__isnull=True, longitude__isnull=True)
  event_list = [e for e in event_list if e.start_time.date() >= date]
  out_data = json.dumps(
      [{'id': e.pk, 'name': e.name, 'type': e.event_type,
        'lat': e.latitude, 'lng': e.longitude} for e in event_list])

  return HttpResponse(out_data, content_type='application/json')
