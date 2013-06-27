#The following was imported from kegbot's models.py
#It also relies on fields.py & imagespecs.py which is included here.
#===============================================
import datetime
import os
import random

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.utils import timezone

from app import fields
from app import imagespecs

def _pics_file_name(instance, filename):
  rand_salt = random.randrange(0xffff)
  new_filename = '%04x-%s' % (rand_salt, filename)
  return os.path.join('pics', new_filename)

class Picture(models.Model):
  image = models.ImageField(upload_to=_pics_file_name,
      help_text='The image')
  resized = imagespecs.resized
  thumbnail = imagespecs.thumbnail
  small_resized = imagespecs.small_resized
  small_thumbnail = imagespecs.small_thumbnail

  time = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return 'Picture: %s' % self.image

class BeerDBModel(models.Model):
  class Meta:
    abstract = True
  added = models.DateTimeField(default=timezone.now, editable=False)
  edited = models.DateTimeField(editable=False)
  beerdb_id = models.CharField(blank=True, null=True, max_length=128)

  def save(self, *args, **kwargs):
    self.edited = timezone.now()
    super(BeerDBModel, self).save(*args, **kwargs)


class Brewer(BeerDBModel):
  """Describes a producer of beer."""
  PRODUCTION_CHOICES = (
    ('commercial', 'Commercial brewer'),
    ('homebrew', 'Home brewer'),
  )

  name = models.CharField(max_length=255,
      help_text='Name of the brewer',
      unique=True)
  country = fields.CountryField(default='USA',
      help_text='Country of origin')
  origin_state = models.CharField(max_length=128,
      default='', blank=True, null=True,
      help_text='State of origin, if applicable')
  origin_city = models.CharField(max_length=128, default='', blank=True,
      null=True,
      help_text='City of origin, if known')
  production = models.CharField(max_length=128, choices=PRODUCTION_CHOICES,
      default='commercial')
  url = models.URLField(default='', blank=True, null=True,
      help_text='Brewer\'s home page')
  description = models.TextField(default='', blank=True, null=True,
      help_text='A short description of the brewer')
  image = models.ForeignKey('Picture', blank=True, null=True,
      related_name='beer_brewers', on_delete=models.SET_NULL)

  def __str__(self):
    return self.name


class BeerStyle(BeerDBModel):
  """Describes a named style of beer (Stout, IPA, etc)"""
  name = models.CharField(max_length=128,
      help_text='Name of the beer style',
      unique=True)

  def __str__(self):
    return self.name


class BeerType(BeerDBModel):
  """Describes a specific kind of beer, by name, brewer, and style."""
  name = models.CharField(max_length=255,
      help_text='Name of the beer; typically unique within a Brewer.',
      unique=True)
  brewer = models.ForeignKey(Brewer,
      help_text='Brewer producing this beer.')
  style = models.ForeignKey(BeerStyle,
      help_text='Style of the beer.')
  edition = models.CharField(max_length=255, blank=True, null=True,
      help_text='For seasonal or special edition beers, the year or '
          'other name uniquely identifying it.')
  abv = models.FloatField(blank=True, null=True,
      help_text='Alcohol by volume, as percentage (0-100).')
  calories_oz = models.FloatField(blank=True, null=True,
      help_text='Calories per fluid ounce of beer.')
  carbs_oz = models.FloatField(blank=True, null=True,
      help_text='Carbohydrates per fluid ounce of beer.')
  original_gravity = models.FloatField(blank=True, null=True,
      help_text='Original gravity of the beer.')
  specific_gravity = models.FloatField(blank=True, null=True,
      help_text='Specific/final gravity of the beer.')
  image = models.ForeignKey('Picture', blank=True, null=True,
      related_name='beer_types', on_delete=models.SET_NULL,
      help_text='Logo or artwork for this beer type.')
  untappd_beer_id = models.IntegerField(blank=True, null=True,
      help_text='Untappd.com beer id for this beer, if known')

  def __str__(self):
    return "%s by %s" % (self.name, self.brewer)

  def GetImage(self):
    if self.image:
      return self.image
    if self.brewer.image:
      return self.brewer.image
    return None
