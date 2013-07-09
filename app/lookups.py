from selectable.base import ModelLookup
from selectable.registry import registry, LookupAlreadyRegistered
from app import models

class BeerTypeLookup(ModelLookup):
  model = models.BeerType
  search_fields = ('name__icontains',)

class BrewerLookup(ModelLookup):
  model = models.Brewer
  search_fields = ('name__icontains',)

try:
  registry.register(BeerTypeLookup)
except LookupAlreadyRegistered:
  pass

try:
  registry.register(BrewerLookup)
except LookupAlreadyRegistered:
  pass