from django.conf.urls import patterns, url

from shipments import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<shipment_id>\d+)/$', views.getShipment, name='detail'),
    url(r'^(?P<shipment_id>\d+)/create/$', views.create_shipment, name='create_shipment'),
)
