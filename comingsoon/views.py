from django.shortcuts import render
from django.template import RequestContext
from groups.models import Group

def index(request):
  return render(request, 'comingsoon/index.html',
      dictionary={'group_count': Group.objects.count()},
      context_instance=RequestContext(request))

def about(request):
  return render(request, 'comingsoon/about.html',
      context_instance=RequestContext(request))
