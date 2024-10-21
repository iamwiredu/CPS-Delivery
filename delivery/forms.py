from django.forms import ModelForm
from .models import DeliveryRequest, BulkDeliveryPoint, BulkDeliveryRequest, Side



class DeliveryRequestForm(ModelForm):
    class Meta:
        model = DeliveryRequest
        labels = {
            "orderQuantity":"Quantity:",
            "pickupNumber":"Sender's Number:",
            "pickupPoint":"Pickup Point:",
            "dropoffNumber":"Receiver's Number:",
            "deliveryPoint":"Dropoff Point:",
            "additionalInfo":"Additional Info:",
            "dropoffLocation":"Dropoff Location:",
            "pickupLocation":"Pickup Location:",
            "product": "Product:",
            "dropoffName":"Reeceiver's Name:",
            "deliverySpeed":"Delivery Speed:",
        }
        fields = ['orderQuantity','product','pickupNumber','pickupPoint','pickupLocation','dropoffName','dropoffNumber','deliveryPoint','dropoffLocation','deliverySpeed','additionalInfo']

class BulkDeliveryRequestForm(ModelForm):
    class Meta:
        model = BulkDeliveryRequest
        fields = ['product','pickupNumber','pickupPoint','pickupLocation',]
        labels ={
            'product':'Product:',
            'pickupNumber':"Sender's Number:",
            'pickupPoint': 'Pickup Point:',
            'pickupLocation':'Pickup Location:',
            
        }
    
class BulkDeliveryPointForm(ModelForm):
    class Meta:
        model = BulkDeliveryPoint
        fields = ['dropoffNumber','dropoffName','deliveryPoint','deliveryLocation','deliverySpeed','additionalInfo']

class SideForm(ModelForm):
    class Meta:
        model = Side
        fields = ['name']
