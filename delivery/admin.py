from django.contrib import admin
from .models import DeliveryRequest, Rider,BulkDeliveryPoint, BulkDeliveryRequest
# Register your models here.

admin.site.register(DeliveryRequest)
admin.site.register(BulkDeliveryRequest)
admin.site.register(BulkDeliveryPoint)
admin.site.register(Rider)