from django.db import models
from django.contrib.auth.models import User
from delivery.models import Rider
# Create your models here.
class Restaurant(models.Model):
    restaurantName = models.CharField(max_length=255)
    restaurantLocation = models.CharField(max_length=255)

class Profile(models.Model):
    class AccountType(models.TextChoices):
        Rider = 'Rider','Rider'
        Restaurant = 'Restaurant', 'Restaurant'
        Nuser = 'Nuser', 'Nuser'
        Nadmin = 'Nadmin', 'Nadmin'

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone = models.CharField(max_length=255)
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE,default=None,null=True,blank=True)
    accountType = models.CharField(choices=AccountType.choices,default=AccountType.Nuser,max_length=10)
    rider = models.OneToOneField(Rider,on_delete=models.CASCADE,default=None,null=True,blank=True)





