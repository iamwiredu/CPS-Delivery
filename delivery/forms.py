from django.forms import ModelForm
from .models import DeliveryRequest




class DeliveryRequestForm(ModelForm):
    class Meta:
        model = DeliveryRequest
        labels = {
            "orderQuantity":"Quantity",
            "pickupNumber":"Pickup Number",
            "pickupPoint":"Pickup Point",
            "dropoffNumber":"Dropoff Number",
            "deliveryPoint":"Dropoff Point",
            "productFee":"Product Fee",
            "additionalInfo":"Additional Info",
        }
        fields = ['orderQuantity','pickupNumber','pickupPoint','dropoffNumber','deliveryPoint','productFee','additionalInfo']
