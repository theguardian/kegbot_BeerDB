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

  new_image = forms.ImageField(required=False,
    help_text='Set/replace image for this beer type.')

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
      Field('new_image'),
      FormActions(
          Submit('submit', 'Save', css_class='btn-primary'),
      )
  )

class BrewerForm(forms.ModelForm):
  class Meta:
    model = models.Brewer
    fields = ('name', 'country', 'origin_state', 'origin_city',
        'production', 'url', 'description')

  new_image = forms.ImageField(required=False,
    help_text='Set/replace image for this brewer.')

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
      Field('new_image'),
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

class ConfirmBrewerDelete(forms.ModelForm):
  class Meta:
    model = models.Brewer

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('name', css_class='input-xlarge'),
      FormActions(
          Submit('submit', 'Delete', css_class='btn-primary'),
      )
  )

class ConfirmBeerStyleDelete(forms.ModelForm):
  class Meta:
    model = models.BeerStyle

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('name', css_class='input-xlarge'),
      FormActions(
          Submit('submit', 'Delete', css_class='btn-primary'),
      )
  )


class ConfirmBeerTypeDelete(forms.ModelForm):
  class Meta:
    model = models.BeerType

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('name', css_class='input-xlarge'),
      FormActions(
          Submit('submit', 'Delete', css_class='btn-primary'),
      )
  )

class ConfirmImagesDelete(forms.ModelForm):
  class Meta:
    model = models.Picture

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('', css_class='input-xlarge'),
      FormActions(
          Submit('submit', 'Delete', css_class='btn-primary'),
      )
  )

class ConfirmMultipleBeerStyleDelete(forms.ModelForm):
  class Meta:
    model = models.BeerStyle

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('', css_class='input-xlarge'),
      FormActions(
          Submit('submit', 'Delete', css_class='btn-primary'),
      )
  )

class ConfirmMultipleBrewerDelete(forms.ModelForm):
  class Meta:
    model = models.Brewer

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('', css_class='input-xlarge'),
      FormActions(
          Submit('submit', 'Delete', css_class='btn-primary'),
      )
  )

class ConfirmMultipleBeerTypeDelete(forms.ModelForm):
  class Meta:
    model = models.BeerType

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('', css_class='input-xlarge'),
      FormActions(
          Submit('submit', 'Delete', css_class='btn-primary'),
      )
  )

class ImportCSV(forms.Form):

  new_file = forms.FileField(required=True,
    help_text='Upload CSV.')

  helper = FormHelper()
  helper.form_class = 'form-horizontal'
  helper.layout = Layout(
      Field('new_file'),
      FormActions(
          Submit('submit', 'Submit', css_class='btn-primary'),
      )
  )