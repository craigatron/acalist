from groups import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^map$', views.group_map, name='group_map'),
    url(r'^heatmap$', views.heatmap, name='group_heatmap'),
)
