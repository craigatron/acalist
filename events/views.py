import datetime
import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.utils import timezone
from django.views.decorators.http import require_GET
from models import Event


@require_GET
def events_list(request):
  event_list = Event.objects.all()
  future_events = get_future_events(event_list)
  future_events.sort(key=lambda e: e.start_time if e.start_time else datetime.datetime.combine(e.start_date, datetime.time(0, 0, 0, 0, timezone.utc)))

  paginator = Paginator(future_events, 20)
  page = request.GET.get('page')
  try:
    events = paginator.page(page)
  except PageNotAnInteger:
    events = paginator.page(1)
  except EmptyPage:
    events = paginator.page(paginator.num_pages)

  return render(request, 'events/event_list.html',
      dictionary={'events': events},
      context_instance=RequestContext(request))

@require_GET
def event_locations(request):
  event_list = Event.objects.exclude(latitude__isnull=True, longitude__isnull=True)
  event_type = request.GET.get('type')
  if event_type:
    try:
      event_list = event_list.filter(event_type__exact=int(event_type))
    except ValueError:
      pass
  future_events = get_future_events(event_list)

  out_data = json.dumps(
      [{'id': e.pk, 'name': e.name, 'type': e.event_type,
        'lat': e.latitude, 'lng': e.longitude} for e in future_events])

  return HttpResponse(out_data, content_type='application/json')

@require_GET
def event_info(request, event_id=None):
  event = get_object_or_404(Event, pk=event_id)
  names = [g.name for g in event.groups.all()]
  return render(request, 'events/event_info.html', dictionary={'event': event, 'names': names},
      context_instance=RequestContext(request))

@require_GET
def event_map(request):
  return render(request, 'events/event_map.html',
      dictionary={'include_oms': 1, 'include_clusterer': 1},
      context_instance=RequestContext(request))


def get_future_events(event_list):
  date = datetime.datetime.now().date()
  future_events = []
  for e in event_list:
    if not e.start_date and not e.start_time:
      continue
    event_date = e.start_date if e.start_date else e.start_time.date()
    if event_date >= date:
      future_events.append(e)
  return future_events
