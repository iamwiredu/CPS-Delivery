from django.forms import ModelForm
from .models import DeliveryRequest, BulkDeliveryPoint, BulkDeliveryRequest, Side



class DeliveryRequestForm(ModelForm):
    class Meta:
        model = DeliveryRequest
        labels = {
            "orderQuantity":"Quantity:",
            "pickupNumber":"Pickup Number:",
            "pickupPoint":"Pickup Point:",
            "dropoffNumber":"Dropoff Number:",
            "deliveryPoint":"Dropoff Point:",
            "productFee":"Product Fee:",
            "additionalInfo":"Additional Info:",
            "dropoffLocation":"Dropoff Location:",
            "pickupLocation":"Pickup Location:",
            "product": "Product:",
            "dropoffName":'Dropoff Name:'
        }
        fields = ['orderQuantity','product','pickupNumber','pickupPoint','pickupLocation','dropoffName','dropoffNumber','deliveryPoint','dropoffLocation','productFee','additionalInfo']

class BulkDeliveryRequestForm(ModelForm):
    class Meta:
        model = BulkDeliveryRequest
        fields = ['product','pickupNumber','pickupPoint','pickupLocation','productFee']
        labels ={
            'product':'Product:',
            'pickupNumber':'Pickup Number:',
            'pickupPoint': 'Pickup Point:',
            'pickupLocation':'Pickup Location:',
            'productFee': 'Product Fee:',
        }
        helptext ={
            'productFee':'price per product'
        }

class BulkDeliveryPointForm(ModelForm):
    class Meta:
        model = BulkDeliveryPoint
        fields = ['dropoffNumber','dropoffName','deliveryPoint','deliveryLocation','additionalInfo']

class SideForm(ModelForm):
    class Meta:
        model = Side
        fields = ['name']
