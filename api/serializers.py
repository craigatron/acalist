from groups import models
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Group
    fields = ('name', 'location', 'latitude', 'longitude')
