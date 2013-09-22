import json
import logging
import urllib2

from groups.models import Group

def search_fb_profiles(search, types=None, makeups=None):
  count = 0
  hit = 0

  queryset = Group.objects.filter(facebook_id__isnull=False).exclude(facebook_id__exact='')
  if types:
    if isinstance(types, list):
      queryset = queryset.filter(group_type__in=types)
    else:
      queryset = queryset.filter(group_type__exact=int(types))
  if makeups:
    if isinstance(makeups, list):
      queryset = queryset.filter(makeups__in=makeups)
    else:
      queryset = queryset.filter(makeups__exact=int(makeups))
  for group in queryset:
    # some groups somehow still haven't picked a page ID
    facebook_id = group.facebook_id.split('/')[-1]
    try:
      data = json.load(
          urllib2.urlopen('https://graph.facebook.com/' + facebook_id))
      about = data.get('about', '').lower()
      description = data.get('description', '').lower()
      bio = data.get('bio', '').lower()
      if search in about or search in description or search in bio:
        hit += 1
      count += 1
    except urllib2.HTTPError:
      logging.error('Error fetching facebook ID %s', facebook_id)
  return hit, count
