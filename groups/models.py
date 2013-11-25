from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=255)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ('name',)


class Group(models.Model):
  TYPES = (
      (0, 'scholastic'),
      (1, 'collegiate'),
      (2, 'semi-professional'),
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
  location = models.TextField(null=True, blank=True)
  latitude = models.FloatField(null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)
  website = models.URLField(null=True, blank=True)
  email = models.EmailField(max_length=255, null=True, blank=True)

  # Social media stuff
  bajigga_id = models.CharField(max_length=255, null=True, blank=True)
  facebook_id = models.CharField(max_length=255, null=True, blank=True)
  gplus_id = models.CharField(max_length=255, null=True, blank=True)
  myspace_id = models.CharField(max_length=255, null=True, blank=True)
  soundcloud_id = models.CharField(max_length=255, null=True, blank=True)
  spotify_id = models.CharField(max_length=255, null=True, blank=True)
  tumblr_id = models.CharField(max_length=255, null=True, blank=True)
  twitter_id = models.CharField(max_length=30, null=True, blank=True)
  wikipella_id = models.CharField(max_length=255, null=True, blank=True)
  youtube_id = models.CharField(max_length=255, null=True, blank=True)
  loudr_id = models.CharField(max_length=255, null=True, blank=True)
  instagram_id = models.CharField(max_length=255, null=True, blank=True)
  itunes_id = models.CharField(max_length=255, null=True, blank=True)

  makeup = models.IntegerField(choices=MAKEUPS)
  is_auditioning = models.BooleanField()

  tags = models.ManyToManyField(Tag, null=True, blank=True)

  def __unicode__(self):
    return self.name

  class Meta:
    ordering = ('name',)
