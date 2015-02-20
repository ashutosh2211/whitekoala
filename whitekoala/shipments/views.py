from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from shipments.serializers import ShipmentSerializer
from rest_framework.parsers import JSONParser

from django.http import HttpResponse

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getShipment(request, shipment_id):
    return HttpResponse("You're looking at shipment %s." % shipment_id)

@csrf_exempt
def create_shipment(request , shipment_id) :
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print data
        #shipment = Shipment(shipment_id=shipment_id)
        serializer = ShipmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Oh")
        return HttpResponse("Ah")
            #return JSONResponse(serializer.data, status=201)


    #received_json_data = json.loads(request.body)
