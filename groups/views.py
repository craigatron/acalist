from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_GET
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
