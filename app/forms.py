#This file is modified from pykeg/web/kegadmin/forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Hidden, Div
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from app import models

class BeerTypeForm(forms.ModelForm):
  class Meta:
    model = models.BeerType
    fields = ('name', 'style', 'brewer', 'edition', 'abv',
        'calories_oz', 'carbs_oz', 'original_gravity', 'specific_gravity',
        'untappd_beer_id')

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('name', css_class='input-xlarge'),
      Field('style', css_class='input-xlarge'),
      Field('brewer'),
      Field('edition'),
      Field('abv'),
      Field('calories_oz'),
      Field('carbs_oz'),
      Field('original_gravity'),
      Field('specific_gravity'),
      Field('untappd_beer_id'),
      FormActions(
          Submit('submit', 'Save', css_class='btn-primary'),
      )
  )

class BrewerForm(forms.ModelForm):
  class Meta:
    model = models.Brewer

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('name', css_class='input-xlarge'),
      Field('country', css_class='input-xlarge'),
      Field('origin_state', css_class='input-xlarge'),
      Field('origin_city', css_class='input-xlarge'),
      Field('production'),
      Field('url'),
      Field('description'),
      Field('image'),
      FormActions(
          Submit('submit', 'Save', css_class='btn-primary'),
      )
  )

class BeerStyleForm(forms.ModelForm):
  class Meta:
    model = models.BeerStyle

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('name', css_class='input-xlarge'),
      FormActions(
          Submit('submit', 'Save', css_class='btn-primary'),
      )
  )
