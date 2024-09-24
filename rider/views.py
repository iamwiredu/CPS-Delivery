from django.shortcuts import render
from delivery.models import DeliveryRequest, BulkDeliveryRequest
from delivery.models import Rider

# Create your views here.


def riderManagement(request,unique_id):
    rider = Rider.objects.get(unique_id=unique_id)

    assignedSingle = DeliveryRequest.objects.filter(rider=rider,delivered=False)
    assignedBulk = BulkDeliveryRequest.objects.filter(rider=rider,delivered=False)
    context = {
        'assignedSingle':assignedSingle,
        'assignedBulk':assignedBulk,
    }
    return render(request,'riderManagement.html',context)


