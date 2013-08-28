from django.contrib import admin
from groups.models import Group

class GroupAdmin(admin.ModelAdmin):
  list_display = ('name', 'location')
  search_fields = ['name', 'location']

admin.site.register(Group, GroupAdmin)
