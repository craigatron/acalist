from events import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.events_list, name='event_list'),
    url(r'^location$', views.event_locations, name='event_locations'),
    url(r'^info/(?P<event_id>[^/]+)', views.event_info, name='event_info'),
    url(r'^map$', views.event_map, name='event_map'),
)
