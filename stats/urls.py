from stats import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.stats, name='stats'),
)
