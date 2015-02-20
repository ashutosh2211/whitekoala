from django.db import models
from djangotoolbox.fields import EmbeddedModelField

class Shipment(models.Model):
    shipment_id =models.CharField(max_length=16)
    from_address = EmbeddedModelField('Address')

class Destinations(models.Model):
    destination_id =models.CharField(max_length=10)
    name  = models.CharField(max_length=30)

class Address(models.Model):
    name  = models.CharField(max_length=30)
    number = models.IntegerField()
    street = models.CharField(max_length=20)

