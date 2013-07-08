import cStringIO
import datetime
import csv
import codecs

from django import forms
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import widgets
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer
from app.serializers import BeerTypeSerializer, BeerStyleSerializer, BrewerSerializer, PictureSerializer
from app import models
from app import forms

def index(request):
  context = RequestContext(request)
  return render_to_response('index.html', context_instance=context)

def beer_type_list(request):
  context = RequestContext(request)
  beers = models.BeerType.objects.all().order_by('name')
  paginator = Paginator(beers, 25)

  page = request.GET.get('page')
  try:
    beers = paginator.page(page)
  except PageNotAnInteger:
    beers = paginator.page(1)
  except EmptyPage:
    beers = paginator.page(paginator.num_pages)

  context['beers'] = beers
  return render_to_response('beer_type_list.html', context_instance=context)


def beer_type_detail(request, beer_id):
  btype = get_object_or_404(models.BeerType, id=beer_id)

  form = forms.BeerTypeForm(instance=btype)
  if request.method == 'POST':
    form = forms.BeerTypeForm(request.POST, instance=btype)
    if form.is_valid():
      btype = form.save()
      new_image = request.FILES.get('new_image')
      if new_image:
        pic = models.Picture.objects.create()
        ext = new_image.name.split('.')[-1]
        pic.image.save(btype.brewer.name+'.'+btype.name+'.'+ext, new_image)
        pic.btype_id = btype.id
        pic.btype_name = btype.name
        pic.brewer_id = btype.brewer
        pic.brewer_name = btype.brewer.name
        pic.save()
        btype.image = pic
        btype.save()
      messages.success(request, 'Beer type updated.')

  context = RequestContext(request)
  context['beer_type'] = btype
  context['form'] = form
  return render_to_response('beer_type_detail.html', context_instance=context)

def beer_type_add(request):
  #btype = get_object_or_404(models.BeerType, id=beer_id)

  form = forms.BeerTypeForm()
  if request.method == 'POST':
    form = forms.BeerTypeForm(request.POST)
    if form.is_valid():
      btype = form.save()
      new_image = request.FILES.get('new_image')
      if new_image:
        pic = models.Picture.objects.create()
        ext = new_image.name.split('.')[-1]
        pic.image.save(btype.brewer.name+'.'+btype.name+'.'+ext, new_image)
        pic.btype_id = btype.id
        pic.btype_name = btype.name
        pic.brewer_id = btype.brewer
        pic.brewer_name = btype.brewer.name
        pic.save()
        btype.image = pic
        btype.save()
      messages.success(request, 'Beer type added.')

  context = RequestContext(request)
  context['beer_type'] = "new"
  context['form'] = form
  return render_to_response('beer_type_add.html', context_instance=context)

def beer_type_remove(request, beer_id):
  btype = get_object_or_404(models.BeerType, id=beer_id)

  form = forms.ConfirmBeerTypeDelete(instance=btype)
  if request.method == 'POST':
    #if form.is_valid():
    models.BeerType.objects.filter(id=beer_id).delete()
    messages.success(request, 'Beer type removed.')

  context = RequestContext(request)
  context['beer_type'] = btype
  context['form'] = form
  return render_to_response('beer_type_remove.html', context_instance=context)

def brewer_list(request):
  context = RequestContext(request)
  brewers = models.Brewer.objects.all().order_by('name')
  paginator = Paginator(brewers, 25)

  page = request.GET.get('page')
  try:
    brewers = paginator.page(page)
  except PageNotAnInteger:
    brewers = paginator.page(1)
  except EmptyPage:
    brewers = paginator.page(paginator.num_pages)

  context['brewers'] = brewers
  return render_to_response('brewer_list.html', context_instance=context)

def brewer_detail(request, brewer_id):
  brewer = get_object_or_404(models.Brewer, id=brewer_id)

  form = forms.BrewerForm(instance=brewer)
  if request.method == 'POST':
    form = forms.BrewerForm(request.POST, instance=brewer)
    if form.is_valid():
      brewer = form.save()
      new_image = request.FILES.get('new_image')
      if new_image:
        pic = models.Picture.objects.create()
        ext = new_image.name.split('.')[-1]
        pic.image.save(brewer.name+'.'+ext, new_image)
        pic.brewer_id = brewer.id
        pic.brewer_name = brewer.name
        pic.save()
        brewer.image = pic
        brewer.save()
      messages.success(request, 'Brewer updated.')

  context = RequestContext(request)
  context['brewer'] = brewer
  context['form'] = form
  return render_to_response('brewer_detail.html', context_instance=context)

def brewer_add(request):
  #brewer = get_object_or_404(models.Brewer, id=brewer_id)

  form = forms.BrewerForm()
  if request.method == 'POST':
    form = forms.BrewerForm(request.POST)
    if form.is_valid():
      brewer = form.save()
      new_image = request.FILES.get('new_image')
      if new_image:
        pic = models.Picture.objects.create()
        ext = new_image.name.split('.')[-1]
        pic.image.save(brewer.name+'.'+ext, new_image)
        pic.brewer_id = brewer.id
        pic.brewer_name = brewer.name
        pic.save()
        brewer.image = pic
        brewer.save()
      messages.success(request, 'Brewer added.')

  context = RequestContext(request)
  context['brewer'] = "new"
  context['form'] = form
  return render_to_response('brewer_add.html', context_instance=context)

def brewer_remove(request, brewer_id):
  brewer = get_object_or_404(models.Brewer, id=brewer_id)

  form = forms.ConfirmBrewerDelete(instance=brewer)
  if request.method == 'POST':
    #if form.is_valid():
    models.Brewer.objects.filter(id=brewer_id).delete()
    messages.success(request, 'Brewer removed.')

  context = RequestContext(request)
  context['brewer'] = brewer
  context['form'] = form
  return render_to_response('brewer_remove.html', context_instance=context)


def beer_style_list(request):
  context = RequestContext(request)
  styles = models.BeerStyle.objects.all().order_by('name')
  paginator = Paginator(styles, 25)

  page = request.GET.get('page')
  try:
    styles = paginator.page(page)
  except PageNotAnInteger:
    styles = paginator.page(1)
  except EmptyPage:
    styles = paginator.page(paginator.num_pages)

  context['styles'] = styles
  return render_to_response('beer_style_list.html', context_instance=context)

def beer_style_detail(request, style_id):
  style = get_object_or_404(models.BeerStyle, id=style_id)

  form = forms.BeerStyleForm(instance=style)
  if request.method == 'POST':
    form = forms.BeerStyleForm(request.POST, instance=style)
    if form.is_valid():
      form.save()
      messages.success(request, 'Beer style updated.')

  context = RequestContext(request)
  context['style'] = style
  context['form'] = form
  return render_to_response('beer_style_detail.html', context_instance=context)

def beer_style_add(request):
  #style = get_object_or_404(models.BeerStyle, id=style_id)

  form = forms.BeerStyleForm()
  if request.method == 'POST':
    form = forms.BeerStyleForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Beer style added.')

  context = RequestContext(request)
  context['style'] = "new"
  context['form'] = form
  return render_to_response('beer_style_add.html', context_instance=context)

def beer_style_remove(request, style_id):
  style = get_object_or_404(models.BeerStyle, id=style_id)

  form = forms.ConfirmBeerStyleDelete(instance=style)
  if request.method == 'POST':
    #if form.is_valid():
    models.BeerStyle.objects.filter(id=style_id).delete()
    messages.success(request, 'Beer style removed.')

  context = RequestContext(request)
  context['style'] = style
  context['form'] = form
  return render_to_response('beer_style_remove.html', context_instance=context)

def beer_type_json(request):
  #btype = get_object_or_404(models.BeerType, id=beer_id)

  btype_json = serializers.serialize("json", models.BeerType.objects.all())

  context = RequestContext(request)
  #context['beer_type'] = btype
  return HttpResponse(btype_json, content_type="application/json")

def beer_style_json(request):
  #btype = get_object_or_404(models.BeerType, id=beer_id)

  bstyle_json = serializers.serialize("json", models.BeerStyle.objects.all())

  context = RequestContext(request)
  #context['beer_type'] = btype
  return HttpResponse(bstyle_json, content_type="application/json")

def brewer_json(request):
  #btype = get_object_or_404(models.BeerType, id=beer_id)

  brewer_json = serializers.serialize("json", models.Brewer.objects.all())

  context = RequestContext(request)
  #context['beer_type'] = btype
  return HttpResponse(brewer_json, content_type="application/json")

def tools(request):
  context = RequestContext(request)
  return render_to_response('tools.html', context_instance=context)

def image_list(request):
  context = RequestContext(request)
  images = models.Picture.objects.all().order_by('image')

  form = forms.ConfirmImagesDelete()
  if request.method == 'POST':
    #if form.is_valid():
    models.Picture.objects.all().delete()
    messages.success(request, 'All images removed.')
  
  context['images'] = images
  context['form'] = form
  return render_to_response('images.html', context_instance=context)

def styles_wipe(request):
  context = RequestContext(request)
  styles = models.BeerStyle.objects.all()

  form = forms.ConfirmMultipleBeerStyleDelete()
  if request.method == 'POST':
    #if form.is_valid():
    max_id = models.BeerStyle.objects.latest('id').id
    for x in range(1, max_id+1):
      models.BeerStyle.objects.filter(id=x).delete()
    messages.success(request, 'All Beer Styles removed.')
  
  context['styles'] = styles
  context['form'] = form
  return render_to_response('wipe_styles.html', context_instance=context)

def brewers_wipe(request):
  context = RequestContext(request)
  brewers = models.Brewer.objects.all()

  form = forms.ConfirmMultipleBrewerDelete()
  if request.method == 'POST':
    #if form.is_valid():
    max_id = models.Brewer.objects.latest('id').id
    for x in range(1, max_id+1):
      models.Brewer.objects.filter(id=x).delete()
    messages.success(request, 'All Brewers removed.')
  
  context['brewers'] = brewers
  context['form'] = form
  return render_to_response('wipe_brewers.html', context_instance=context)

def beers_wipe(request):
  context = RequestContext(request)
  btypes = models.BeerType.objects.all().order_by('name')

  form = forms.ConfirmMultipleBeerTypeDelete()
  if request.method == 'POST':
    #if form.is_valid():
    max_id = models.BeerType.objects.latest('id').id
    for x in range(1, max_id+1):
      models.BeerType.objects.filter(id=x).delete()
    messages.success(request, 'All Beer Types removed.')
  
  context['btypes'] = btypes
  context['form'] = form
  return render_to_response('wipe_beers.html', context_instance=context)

def csv_import(request):
  
  form = forms.ImportCSV()
  if request.method == 'POST':
    form = forms.ImportCSV(request.POST, request.FILES)
    if form.is_valid():
      new_file = request.FILES.get('new_file')
      entry_count = 0;
      num_entries = 0;
      if new_file.name == 'styles.csv':
        records = csv.DictReader(new_file)
        for line in records:
          if line['name'] != '':
            num_entries += 1
            try:
              style = models.BeerStyle.objects.get(name=line['name'])
            except:
              style = models.BeerStyle.objects.create()
              style.name = line['name']
              style.save()
              entry_count += 1
        messages.success(request, str(entry_count)+' of '+str(num_entries)+' Beer Styles Imported.')
      elif new_file.name == 'breweries.csv':
        records = csv.DictReader(new_file)
        for line in records:
          if line['name'] != '':
            num_entries += 1
            try:
              brewer = models.Brewer.objects.get(name=line['name'])
            except:
              brewer = models.Brewer.objects.create()
              brewer.name = line['name']
              brewer.country = line['country']
              brewer.origin_state = line['origin_state']
              brewer.origin_city = line['origin_city']
              brewer.production = line['production']
              brewer.url = line['url']
              brewer.description = line['description']
              brewer.save()
              entry_count += 1
        messages.success(request, str(entry_count)+' of '+str(num_entries)+' Brewers Imported.')
      elif new_file.name == 'beers.csv':
        records = csv.DictReader(new_file)
        for line in records:
          if line['name'] != '':
            num_entries += 1
            try:
              btype = models.BeerType.objects.get(name=line['name'], brewer_id=line['brewer'], edition=line['edition'])
            except:
              btype = models.BeerType.objects.create(brewer_id=line['brewer'], style_id=line['style'])
              btype.name = line['name']
              btype.edition = line['edition']
              btype.description = line['description']
              if line['abv'] != '':
                btype.abv = float(line['abv'])
              if line['calories_oz'] != '':
                btype.calories_oz = float(line['calories_oz'])
              if line['carbs_oz'] != '':
                btype.carbs_oz = float(line['carbs_oz'])
              if line['original_gravity'] != '':
                btype.original_gravity = float(line['original_gravity'])
              if line['specific_gravity'] != '':
                btype.specific_gravity = float(line['specific_gravity'])
              if line['untappd_beer_id'] != '':
                btype.untappd_beer_id = int(line['untappd_beer_id'])
              btype.save()
              entry_count += 1
        messages.success(request, str(entry_count)+' of '+str(num_entries)+' Beer Types Imported.')
      else:
        messages.success(request, 'Nothing Imported. Try using a compatible filename.')

  context = RequestContext(request)
  context['style'] = "new"
  context['form'] = form
  return render_to_response('csv_import.html', context_instance=context)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BeersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.BeerType.objects.all()
    serializer_class = BeerTypeSerializer

    def get_queryset(self):
      queryset = models.BeerType.objects.all()
      btype= self.request.QUERY_PARAMS.get('name', None)
      if btype is not None:
        queryset = queryset.filter(name__contains=btype)
      return queryset

class BeerStyleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.BeerStyle.objects.all()
    serializer_class = BeerStyleSerializer

    def get_queryset(self):
      queryset = models.BeerStyle.objects.all()
      bstyle= self.request.QUERY_PARAMS.get('id', None)
      if bstyle is not None:
        queryset = queryset.filter(id=bstyle)
      return queryset

class BrewerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Brewer.objects.all()
    serializer_class = BrewerSerializer

    def get_queryset(self):
      queryset = models.Brewer.objects.all()
      brewer = self.request.QUERY_PARAMS.get('id', None)
      if brewer is not None:
        queryset = queryset.filter(id=brewer)
      return queryset

class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Picture.objects.all()
    serializer_class = PictureSerializer

    def get_queryset(self):
      queryset = models.Picture.objects.all()
      picture = self.request.QUERY_PARAMS.get('id', None)
      if picture is not None:
        queryset = queryset.filter(id=picture)
      return queryset
