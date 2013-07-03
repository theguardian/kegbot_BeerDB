from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BeerTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BeerType
		#fields = ('name', 'style', 'brewer', 'edition', 'abv',
			#'calories_oz', 'carbs_oz', 'original_gravity', 'specific_gravity',
			#'untappd_beer_id')

class BeerStyleSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BeerStyle
		#field = 'name'


class BrewerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Brewer
		#fields = ('name', 'country', 'origin_state', 'origin_city',
			#'production', 'url', 'description', 'image')

class PictureSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Picture