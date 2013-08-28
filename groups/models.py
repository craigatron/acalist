from django.db import models

class Group(models.Model):
  TYPES = (
      (0, 'scholastic'),
      (1, 'collegiate'),
      (2, 'casual'),
      (3, 'professional'),
      (4, 'other'),
  )
  MAKEUPS = (
      (0, 'all-male'),
      (1, 'all-female'),
      (2, 'mixed'),
  )
  name = models.CharField(max_length=255)
  group_type = models.IntegerField(choices=TYPES)
  location = models.TextField()
  latitude = models.FloatField()
  longitude = models.FloatField()
  website = models.URLField(null=True, blank=True)
  email = models.EmailField(max_length=255, null=True, blank=True)
  wikipella_url = models.URLField(null=True, blank=True)
  facebook_id = models.CharField(max_length=255, null=True, blank=True)
  twitter_id = models.CharField(max_length=30, null=True, blank=True)
  youtube_id = models.CharField(max_length=255, null=True, blank=True)
  gplus_id = models.CharField(max_length=255, null=True, blank=True)
  myspace_id = models.CharField(max_length=255, null=True, blank=True)
  makeup = models.IntegerField(choices=MAKEUPS)
  is_auditioning = models.BooleanField()

  def __unicode__(self):
    return self.name
