from django.forms import ModelForm
from .models import DeliveryRequest




class DeliveryRequestForm(ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = ['orderQuantity','pickupNumber','pickupPoint','dropoffNumber','deliveryPoint','productFee','additionalInfo']
