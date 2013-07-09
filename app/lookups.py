from selectable.base import ModelLookup
from selectable.registry import registry, LookupAlreadyRegistered
from app import models

class BeerTypeLookup(ModelLookup):
  model = models.BeerType
  search_field = 'name__contains'

try:
  registry.register(BeerTypeLookup)
except LookupAlreadyRegistered:
  pass