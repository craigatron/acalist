from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.http import require_GET

@require_GET
def group_map(request):
  return render(request, 'groups/map.html',
      dictionary={'include_oms': 1},
      context_instance=RequestContext(request))
