from django.shortcuts import render
from django.template import RequestContext

def index(request):
  return render(request, 'comingsoon/index.html',
      context_instance=RequestContext(request))
