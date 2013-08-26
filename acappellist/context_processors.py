from django.conf import settings

def debug(context):
  return {'PRODUCTION': settings.PRODUCTION}
