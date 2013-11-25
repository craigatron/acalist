from math import asin, cos, radians, sin, sqrt
import simplejson
import urllib
import urllib2

from django.db.models import Count, Q
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.utils.html import escape
from django.views.decorators.http import require_GET
from groups.forms import SearchForm
from groups.models import Group

@require_GET
def group_map(request):
  return render(request, 'groups/map.html',
      dictionary={'include_oms': 1, 'include_clusterer': 1},
      context_instance=RequestContext(request))


@require_GET
def heatmap(request):
  return render(request, 'groups/heatmap.html',
      dictionary={'heatmap': 1}, context_instance=RequestContext(request))


@require_GET
def group_info(request, group_id=None):
  group = get_object_or_404(Group, pk=group_id)
  return render(request, 'groups/group_info.html', dictionary={'group': group},
      context_instance=RequestContext(request))


@require_GET
def group_list(request):
  group_list = Group.objects.all()
  if any([x in request.GET for x in ['group_type', 'makeup', 'search']]):
    form = SearchForm(request.GET)
    if form.is_valid():
      data = form.cleaned_data
      if data.get('group_type'):
        group_list = group_list.filter(group_type=data['group_type'])
      if data.get('makeup'):
        group_list = group_list.filter(makeup=data['makeup'])
      if data.get('search'):
        query = data.get('search')
        group_list = group_list.filter(
            Q(name__icontains=query) | Q(location__icontains=query))
      if data.get('location'):
        geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
        location = escape(data.get('location'))
        loc_data = simplejson.load(urllib2.urlopen(geocode_url + '?' +
            urllib.urlencode({'sensor': 'false', 'address': location})))
        if (loc_data.get('results') and loc_data['results'][0].get('geometry')
            and loc_data['results'][0]['geometry'].get('location')):
          latlng = loc_data['results'][0]['geometry']['location']
          group_list = geo_filter(group_list, latlng['lat'], latlng['lng'],
              data.get('distance'), data.get('unit'))
    elif request.GET.get('search'):
      # hopefully temporary hack here
      query = request.GET.get('search')
      group_list = group_list.filter(
          Q(name__icontains=query) | Q(location__icontains=query))
  else:
    form = SearchForm()

  if isinstance(group_list, list):
    group_list.sort(key=lambda x: x.name)
  else:
    group_list = group_list.order_by('name')

  paginator = Paginator(group_list, 20)
  page = request.GET.get('page')
  try:
    groups = paginator.page(page)
  except PageNotAnInteger:
    groups = paginator.page(1)
  except EmptyPage:
    groups = paginator.page(paginator.num_pages)

  return render(request, 'groups/group_list.html',
      dictionary={'groups': groups, 'form': form},
      context_instance=RequestContext(request))

def geo_filter(queryset, lat, lng, distance, dist_unit):
  mult = 69.172 if dist_unit == '0' else 111.322
  r = 3959 if dist_unit == '0' else 6371
  dist = float(distance)
  minlon = lng - (dist / abs(cos(radians(lat)) * mult))
  maxlon = lng + (dist / abs(cos(radians(lat)) * mult))
  minlat = lat - (dist / mult)
  maxlat = lat + (dist / mult)

  queryset = queryset.exclude(latitude__lt=minlat).exclude(
      latitude__gt=maxlat).exclude(longitude__lt=minlon).exclude(
      longitude__gt=maxlon)
  # THIS IS BAD AND I NEED TO CHANGE IT
  new_list = []
  for group in queryset:
    grouplat = group.latitude
    grouplng = group.longitude
    if not grouplat or not grouplng:
      continue

    dlat = radians(grouplat - lat)
    dlon = radians(grouplng - lng)
    lat1 = radians(lat)
    lat2 = radians(grouplat)
    a = sin(dlat / 2) * sin(dlat / 2) + sin(dlon / 2) * sin(dlon / 2) * cos(lat1) * cos(lat2)
    c = 2 * asin(sqrt(a))
    if (r * c < distance):
      new_list.append(group)
  return new_list


@require_GET
def group_locations(request):
  group_list = Group.objects.exclude(latitude__isnull=True, longitude__isnull=True)
  if 'collapse' in request.GET and request.GET['collapse'].lower() == 'true':
    group_list = group_list.values('latitude', 'longitude').annotate(count=Count('id'))
    out_data = simplejson.dumps(
        [{'lat': g['latitude'], 'lng': g['longitude'], 'cnt': g['count']} for g in group_list])
  else:
    out_data = simplejson.dumps(
        [{'id': g.pk, 'name': g.name, 'type': g.group_type,
          'lat': g.latitude, 'lng': g.longitude} for g in group_list])

  return HttpResponse(out_data, mimetype='application/json')
