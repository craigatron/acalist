from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


@require_GET
def group_list(request):
  if 'search' in request.GET:
    query = request.GET['search']
    group_list = Group.objects.filter(
        Q(name__icontains=query) | Q(location__icontains=query))
  else:
    group_list = Group.objects.all()

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
      dictionary={'groups': groups}, context_instance=RequestContext(request))
