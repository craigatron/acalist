from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
  filter_horizontal = ('groups',)
  list_display = ('name', 'location')
  search_fields = ['name', 'location', 'groups__name']

admin.site.register(Event, EventAdmin)
