from groups import models
from rest_framework import viewsets
from api import serializers

class GroupViewSet(viewsets.ModelViewSet):
  queryset = models.Group.objects.all()
  serializer_class = serializers.GroupSerializer
