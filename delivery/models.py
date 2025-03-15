import uuid
import requests
from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Restaurant, Food


class Rider(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    assigned = models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None,null=True,related_name='rider')

    def __str__(self):
        return f'{self.name}'
    
class CartRestaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    @property
    def total_price(self):
        items = self.cart_items.all()
        return sum(item.total_price for item in items)

    @property
    def total_items(self):
        return self.cart_items.count()

class CartItemRestaurant(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    cart = models.ForeignKey(CartRestaurant, related_name='cart_items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.quantity} x {self.food.name}"

   
    @property
    def total_price(self):
        """Calculate the total price including the quantity of food and any sides."""
        main_price = self.food.price * self.quantity
        side_orders = self.sideorder_set.all()  # Ensure it's the correct related name
        for side_order in side_orders:
            main_price += side_order.total()
        return main_price


class RestaurantOrder(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True,blank=True)
    Cart = models.OneToOneField(CartRestaurant,on_delete=models.CASCADE,null=True,blank=True)

class Side(models.Model):
    food = models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/sides',null=True,blank=True,default='images/sides/default.png')

class SideOrder(models.Model):
    side = models.ForeignKey(Side,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    state = models.IntegerField(default=0) # quantity number
    cartItemRestaurant = models.ForeignKey(CartItemRestaurant,on_delete=models.CASCADE,null=True,blank=True)

    def total(self):
        return self.quantity * self.side.price



class DeliveryRequest(models.Model):
    
    class ProductChoices(models.TextChoices):
        FOOD = 'Food', 'Food'
        ITEM = 'item', 'item'

    class DeliveryLocations(models.TextChoices):
        ACCRA = 'Accra', 'Accra'
        KUMASI = 'Kumasi', 'Kumasi'
        CAPE_COAST = 'Cape Coast', 'Cape Coast'
        TAKORADI = 'Takoradi', 'Takoradi'
        KOFORIDUA = 'Koforidua', 'Koforidua'
        HO = 'Ho', 'Ho'
        SUNYANI = 'Sunyani', 'Sunyani'
        TARKWA = 'Tarkwa', 'Tarkwa'
        OBUASI = 'Obuasi', 'Obuasi'
        AKOSOMBO = 'Akosombo', 'Akosombo'
        TECHIMAN = 'Techiman', 'Techiman'
        NSAWAM = 'Nsawam', 'Nsawam'
        NKWAKAW = 'Nkwakaw', 'Nkwakaw'
        WINNEBA = 'Winneba', 'Winneba'
        MANKESSIM = 'Mankessim', 'Mankessim'
        SUHUM = 'Suhum', 'Suhum'
        KONONGO = 'Konongo', 'Konongo'
      
    
    class PickupLocations(models.TextChoices):
        KUMASI = 'Kumasi', 'Kumasi'
    
    class DeliverySpeed(models.TextChoices):
        SAME = 'Same day delivery', 'Same day delivery'
        NEXT = 'Next day delivery', 'Next day delivery'
        EXPRESS = 'Express delivery', 'Express delivery'

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    orderQuantity = models.PositiveIntegerField()
    product = models.CharField(max_length=255,null=True,blank=True, choices=ProductChoices.choices,default=ProductChoices.ITEM)
    pickupNumber = models.PositiveIntegerField()
    deliveryPoint = models.CharField(max_length=10,choices=DeliveryLocations.choices,default=DeliveryLocations.ACCRA)
    dropoffLocation = models.CharField(max_length=255,null=True)
    dropoffNumber = models.PositiveIntegerField()
    dropoffName = models.CharField(max_length=255,null=True)
    pickupPoint = models.CharField(max_length=10, choices=PickupLocations.choices,default=PickupLocations.KUMASI)
    pickupLocation = models.CharField(max_length=255,null=True)
    deliverySpeed = models.CharField(max_length=17,choices=DeliverySpeed.choices,default=DeliverySpeed.SAME)
    additionalInfo = models.TextField(blank=True,null=True)
    delivered = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    enroute = models.BooleanField(default=False)
    pickedUp = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    rider = models.ForeignKey(Rider,on_delete=models.SET_DEFAULT,related_name='assignments',default=None,null=True,blank=True)
    restaurantOrder = models.OneToOneField(RestaurantOrder,default=None,null=True,blank=True,on_delete=models.CASCADE)
    deliveryFee = models.CharField(max_length=255,null=True,blank=True)
    date = models.CharField(max_length=255,default='sdfsadf',null=True)
    @property
    def id_curator(self):    
        id_value = str(self.id)
        start = ''
        if len(id_value) < 4:
            for i in range(4-len(id_value)):
                start += '0'
            return 'S'+str(start+id_value)
        else:
            return 'S'+str(id_value)

def send_sms(sender,instance,created,**kwargs):
    def id_curator(id):
        id_value = str(id)
        start = ''
        if len(id_value) < 4:
            for i in range(4-len(id_value)):
                start += '0'
            return start+id_value
        else:
            return id_value

    if created:
        endPoint = 'https://api.mnotify.com/api/sms/quick'
        apiKey = '	SncBkQH0xepW3ACOlCty3AjUX'
        data = {
        'recipient[]': [str(instance.pickupNumber)],
        'sender': 'CPS',
        'message': f'Your request has been sent waiting for rider assignment .Use  ORDER ID - {id_curator(instance.id)} to track your order.Insist on identification or for help call #0534583364',
        'schedule_date': ''
        }
        url = endPoint + '?key=' + apiKey
        response = requests.post(url, data)
        data = response.json() 
        print(data,str(sender.pickupNumber))


class BulkDeliveryRequest(models.Model):
    class PickupLocations(models.TextChoices):
        KUMASI = 'Kumasi', 'Kumasi'

    class ProductChoices(models.TextChoices):
        FOOD = 'Food', 'Food'
        ITEM = 'item', 'item'



    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    orderQuantity = models.PositiveIntegerField(default=0)
    product = models.CharField(max_length=255,null=True,blank=True, choices=ProductChoices.choices,default=ProductChoices.ITEM)
    pickupNumber = models.PositiveIntegerField()
    pickupPoint = models.CharField(max_length=10, choices=PickupLocations.choices,default=PickupLocations.KUMASI)
    pickupLocation = models.CharField(max_length=255,null=True)
    delivered = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    enroute = models.BooleanField(default=False)
    pickedUp = models.BooleanField(default=False)
    rider = models.ForeignKey(Rider,on_delete=models.SET_DEFAULT,related_name='bulk_assignments',default=None,null=True,blank=True)
    deliveryFee = models.CharField(max_length=255,null=True,blank=True,default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    @property
    def id_curator(self):    
        id_value = str(self.id)
        start = ''
        if len(id_value) < 4:
            for i in range(4-len(id_value)):
                start += '0'
            return 'B'+str(start+id_value)
        else:
            return 'B'+str(id_value)
    
class BulkDeliveryPoint(models.Model):
    class DeliverySpeed(models.TextChoices):
        SAME = 'Same day delivery', 'Same day delivery'
        NEXT = 'Next day delivery', 'Next day delivery'
        EXPRESS = 'Express delivery', 'Express delivery'

    class DeliveryLocations(models.TextChoices):
        ACCRA = 'Accra' 'Accra'
        KUMASI = 'Kumasi', 'Kumasi'
        CAPE_COAST = 'Cape Coast', 'Cape Coast'
        TAKORADI = 'Takoradi', 'Takoradi'
        KOFORIDUA = 'Koforidua', 'Koforidua'
        HO = 'Ho', 'Ho'
        SUNYANI = 'Sunyani', 'Sunyani'
        TARKWA = 'Tarkwa', 'Tarkwa'
        OBUASI = 'Obuasi', 'Obuasi'
        AKOSOMBO = 'Akosombo', 'Akosombo'
        TECHIMAN = 'Techiman', 'Techiman'
        NSAWAM = 'Nsawam', 'Nsawam'
        NKWAKAW = 'Nkwakaw', 'Nkwakaw'
        WINNEBA = 'Winneba', 'Winneba'
        MANKESSIM = 'Mankessim', 'Mankessim'
        SUHUM = 'Suhum', 'Suhum'
        KONONGO = 'Konongo', 'Konongo'
       
    
    bulkDeliveryRequest = models.ForeignKey(BulkDeliveryRequest,related_name='indv_orders',on_delete=models.CASCADE,null=True,blank=True)
    deliveryPoint = models.CharField(max_length=10,choices=DeliveryLocations.choices,default=DeliveryLocations.ACCRA)
    dropoffNumber = models.PositiveIntegerField()
    dropoffName = models.CharField(max_length=255)
    deliveryLocation = models.CharField(max_length=255)
    deliverySpeed = models.CharField(max_length=17,choices=DeliverySpeed.choices,default=DeliverySpeed.SAME)
    additionalInfo = models.TextField(blank=True,null=True)



class QrIdent(models.Model):
    deliveryRequest = models.OneToOneField(DeliveryRequest,on_delete=models.CASCADE,null=True,blank=True)
    bulkDeliveryRequest = models.OneToOneField(BulkDeliveryRequest,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    requestType = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f'{self.id}'