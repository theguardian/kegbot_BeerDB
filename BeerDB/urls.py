from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'beers', views.BeersViewSet)
router.register(r'brewers', views.BrewerViewSet)
router.register(r'beer-styles', views.BeerStyleViewSet)
router.register(r'pictures', views.PictureViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^beers/$', views.beer_type_list, name='beer-types'),
    url(r'^beers/add/$', views.beer_type_add, name='add-beer-type'),
    url(r'^beers/remove/(?P<beer_id>\d+)/$', views.beer_type_remove, name='remove-beer-type'),
    url(r'^beers/(?P<beer_id>\d+)/$', views.beer_type_detail, name='edit-beer-type'),
    url(r'^beer-styles/$', views.beer_style_list, name='beer-styles'),
    url(r'^beer-styles/add/$', views.beer_style_add, name='add-beer-style'),
    url(r'^beer-styles/remove/(?P<style_id>\d+)/$', views.beer_style_remove, name='remove-beer-style'),
    url(r'^beer-styles/(?P<style_id>\d+)/$', views.beer_style_detail, name='edit-beer-style'),
    url(r'^brewers/$', views.brewer_list, name='brewers'),
    url(r'^brewers/add/$', views.brewer_add, name='add-brewer'),
    url(r'^brewers/remove/(?P<brewer_id>\d+)/$', views.brewer_remove, name='remove-brewer'),
    url(r'^brewers/(?P<brewer_id>\d+)/$', views.brewer_detail, name='edit-brewer'),
    url(r'^json/beers/$', views.beer_type_json, name='json-beer-type'),
    url(r'^json/brewer/$', views.brewer_json, name='json-brewer'),
    url(r'^json/beer-styles/$', views.beer_style_json, name='json-beer-style'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    (r'^selectable/', include('selectable.urls')),
    url(r'^tools/$', views.tools, name='tools'),
    url(r'^tools/images/$', views.image_list, name='list-images'),
    url(r'^tools/styles-wipe/$', views.styles_wipe, name='wipe-styles'),
    url(r'^tools/brewers-wipe/$', views.brewers_wipe, name='wipe-brewers'),
    url(r'^tools/beers-wipe/$', views.beers_wipe, name='wipe-beers'),
    url(r'^tools/import/$', views.csv_import, name='import-csv'),
    url(r'^tools/export/$', views.csv_export, name='export-csv'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
