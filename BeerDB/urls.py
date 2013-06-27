from django.conf.urls import patterns, include, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^beers/$', views.beer_type_list, name='beer-types'),
    url(r'^beers/add/$', views.beer_type_add, name='add-beer-type'),
    url(r'^beers/(?P<beer_id>\d+)/$', views.beer_type_detail, name='edit-beer-type'),
    url(r'^beer-styles/$', views.beer_style_list, name='beer-styles'),
    url(r'^beer-styles/add/$', views.beer_style_add, name='add-beer-style'),
    url(r'^beer-styles/(?P<style_id>\d+)/$', views.beer_style_detail, name='edit-beer-style'),
    url(r'^brewers/$', views.brewer_list, name='brewers'),
    url(r'^brewers/add/$', views.brewer_add, name='add-brewer'),
    url(r'^brewers/(?P<brewer_id>\d+)/$', views.brewer_detail, name='edit-brewer'),
)
