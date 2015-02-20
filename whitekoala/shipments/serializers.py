from rest_framework import serializers
from shipments.models import Shipment

class ShipmentSerializer(serializers.Serializer):
    shipment_id =serializers.CharField(required=True, allow_blank=False, max_length=20)
    #promised_delivery_time = serializers.DateTimeField()

    def create(self, validated_data):
        return Shipment.objects.create(**validated_data)


