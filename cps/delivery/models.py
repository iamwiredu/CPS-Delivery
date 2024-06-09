from django.db import models

# Create your models here.

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

    orderQuantity = models.PositiveIntegerField()
    pickupNumber = models.PositiveIntegerField()
    deliveryPoint = models.CharField(max_length=10,choices=DeliveryLocations.choices,default=DeliveryLocations.Select)
    dropoffNumber = models.PositiveIntegerField()
    pickupPoint = models.CharField(max_length=10, choices=DeliveryLocations.choices,default=DeliveryLocations.Select)
    senderNumber = models.PositiveIntegerField()
    productFee = models.FloatField()
    additionalInfo = models.TextField()
    


    