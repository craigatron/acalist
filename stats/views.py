from django.db.models import Count
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.http import require_GET
from groups.models import Group

@require_GET
def stats(request):
  all_makeups = dict((x, y) for x, y in Group.MAKEUPS)
  all_types = dict((x, y) for x, y in Group.TYPES)
  makeups = [['Makeup', 'Count']]
  for makeup in Group.objects.values('makeup').annotate(count=Count('makeup')):
    makeups.append([all_makeups[int(makeup['makeup'])], makeup['count']])
  types = [['Type', 'Count']]
  for group_type in Group.objects.values('group_type').annotate(count=Count('group_type')):
    types.append([all_types[int(group_type['group_type'])], group_type['count']])

  return render(request, 'stats/stats.html',
      dictionary={'genders': str(makeups), 'types': str(types)},
      context_instance=RequestContext(request))
