from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'', include('comingsoon.urls')),
  url(r'events/', include('events.urls')),
  url(r'^groups/', include('groups.urls')),
  url(r'^stats/', include('stats.urls')),
)

urlpatterns += staticfiles_urlpatterns()
