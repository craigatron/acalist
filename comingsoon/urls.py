from comingsoon import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/?$', views.about, name='about'),
)
