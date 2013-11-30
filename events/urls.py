from events import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.events_list, name='event_list'),
    url(r'^location$', views.event_locations, name='event_locations'),
)
