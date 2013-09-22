import simplejson

from django.db.models import Count, Q
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
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
  else:
    form = SearchForm()

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
