import uuid
import requests
from django.db import models
from django.contrib.auth.models import User


class Rider(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    assigned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class DeliveryRequest(models.Model):
    class DeliveryLocations(models.TextChoices):
        Select = 'Select', 'Select'
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
    
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    orderQuantity = models.PositiveIntegerField()
    pickupNumber = models.PositiveIntegerField()
    deliveryPoint = models.CharField(max_length=10,choices=DeliveryLocations.choices,default=DeliveryLocations.Select)
    dropoffNumber = models.PositiveIntegerField()
    pickupPoint = models.CharField(max_length=10, choices=DeliveryLocations.choices,default=DeliveryLocations.Select)
    productFee = models.FloatField()
    additionalInfo = models.TextField()
    delivered = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    enroute = models.BooleanField(default=False)
    pickedUp = models.BooleanField(default=False)
    rider = models.ForeignKey(Rider,on_delete=models.SET_DEFAULT,related_name='assignments',default=None,null=True,blank=True)

    @property
    def id_curator(self):    
        id_value = str(self.id)
        start = ''
        if len(id_value) < 4:
            for i in range(4-len(id_value)):
                start += '0'
            return start+id_value
        else:
            return id_value

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

class ShopItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/shopItems')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class BulkDeliveryRequest(models.Model):
    class DeliveryLocations(models.TextChoices):
        Select = 'Select', 'Select'
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
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    orderQuantity = models.PositiveIntegerField()
    pickupNumber = models.PositiveIntegerField()
    pickupPoint = models.CharField(max_length=10, choices=DeliveryLocations.choices,default=DeliveryLocations.Select)
    productFee = models.FloatField()
    delivered = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    enroute = models.BooleanField(default=False)
    pickedUp = models.BooleanField(default=False)
    rider = models.ForeignKey(Rider,on_delete=models.SET_DEFAULT,related_name='bulk_assignments',default=None,null=True,blank=True)

    
class BulkDeliveryPoint(models.Model):
    class DeliveryLocations(models.TextChoices):
        Select = 'Select', 'Select'
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
    
    bulkDeliveryRequest = models.ForeignKey(BulkDeliveryRequest,on_delete=models.CASCADE,null=True,blank=True)
    deliveryPoint = models.CharField(max_length=10,choices=DeliveryLocations.choices,default=DeliveryLocations.Select)
    dropoffNumber = models.PositiveIntegerField()
    dropoffName = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    additionalInfo = models.TextField()
