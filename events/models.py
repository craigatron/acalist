from django.db import models
from groups.models import Group

class Event(models.Model):
  EVENT_TYPES = (
      (0, 'show'),
      (1, 'festival'),
      (2, 'competition'),
      (3, 'audition'),
      (4, 'caroling'),
  )
  name = models.CharField(max_length=255)
  event_type = models.IntegerField(choices=EVENT_TYPES)
  location = models.TextField(null=True, blank=True)
  latitude = models.FloatField(null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)
  website = models.URLField(null=True, blank=True)
  facebook_event_id = models.CharField(max_length=255, null=True, blank=True)
  start_time = models.DateTimeField(null=True, blank=True)
  # only really relevant for multi-day things
  start_date = models.DateField(null=True, blank=True)
  end_date = models.DateField(null=True, blank=True)
  groups = models.ManyToManyField(Group, null=True, blank=True)
