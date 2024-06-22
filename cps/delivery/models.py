from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
import requests
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField(null=True,blank=True)

class Rider(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    assigned = models.BooleanField(default=False)


class DeliveryRequest(models.Model):
    class DeliveryLocations(models.TextChoices):
        Select = 'Select', 'Select'
        KUMASI = 'Kumasi', 'Kumasi'
        CAPE_COAST = 'Cape Coast', 'Cape Coast'
        TAKORADI = 'Takoradi', 'Takoradi'
        KOTORIDUA = 'Kotoridua', 'Kotoridua'
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
    senderNumber = models.PositiveIntegerField()
    productFee = models.FloatField()
    additionalInfo = models.TextField()
    delivered = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    enroute = models.BooleanField(default=False)
    pickedUp = models.BooleanField(default=False)
    rider = models.ForeignKey(Rider,on_delete=models.SET_DEFAULT,related_name='assignments',default=None,null=True,blank=True)

    

def send_sms(sender,instance,created,**kwargs):
    if created:
        endPoint = 'https://api.mnotify.com/api/sms/quick'
        apiKey = '	SncBkQH0xepW3ACOlCty3AjUX'
        data = {
        'recipient[]': [str(instance.pickupNumber)],
        'sender': 'CPS',
        'message': f'Your request with order id {instance.unique_id} has been created. Waiting Assignment.',
        'is_schedule': False,
        'schedule_date': ''
        }
        url = endPoint + '?key=' + apiKey
        response = requests.post(url, data)
        data = response.json() 
        print(data,str(sender.pickupNumber))

post_save.connect(send_sms,sender=DeliveryRequest)

def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.phone = User.phone
        user_profile.save()

post_save.connect(create_profile, sender=User)


class ShopItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/shopItems')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


