from django.contrib import admin
from .models import DeliveryRequest, Rider,BulkDeliveryPoint, BulkDeliveryRequest, CartItemRestaurant, QrIdent, CartRestaurant, RestaurantOrder, Side, SideOrder
# Register your models here.

admin.site.register(DeliveryRequest)
admin.site.register(BulkDeliveryRequest)
admin.site.register(BulkDeliveryPoint)
admin.site.register(Rider)
admin.site.register(CartItemRestaurant)
admin.site.register(CartRestaurant)
admin.site.register(RestaurantOrder)
admin.site.register(Side)
admin.site.register(SideOrder)
admin.site.register(QrIdent)