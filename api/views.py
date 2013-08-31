from groups import models
from rest_framework import viewsets
from api import serializers

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = models.Group.objects.all()
  serializer_class = serializers.GroupSerializer
