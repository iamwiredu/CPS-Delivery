import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Restaurant(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,related_name='restaurant')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Food(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='foods')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/', default='food_images/images.png',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"

