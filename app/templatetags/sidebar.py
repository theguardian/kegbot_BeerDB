from django import template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import loader, RequestContext
from django import forms
from app import forms

register = template.Library()

@register.simple_tag(takes_context=True)
def sidebar(context):

  request = context['request']
  context = RequestContext(request)

  beer_form = forms.SearchBeerForm(prefix='beer')
  brewer_form = forms.SearchBrewerForm(prefix='brewer')
  return render_to_string('sidebar.html', {'beer_form': beer_form, 'brewer_form': brewer_form}, context_instance=context)