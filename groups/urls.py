from groups import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.group_list, name='group_list'),
    url(r'^map$', views.group_map, name='group_map'),
    url(r'^heatmap$', views.heatmap, name='group_heatmap'),
    url(r'^info/(?P<group_id>[^/]+)', views.group_info, name='group_info'),
    url(r'^location$', views.group_locations, name='group_locations'),
)
