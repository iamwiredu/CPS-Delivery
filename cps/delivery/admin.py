from django.contrib import admin
from .models import DeliveryRequest, Profile, ShopItem
# Register your models here.


admin.site.register(DeliveryRequest)
admin.site.register(Profile)
admin.site.register(ShopItem)