from django.urls import path
from .views import requestPage, homePage

urlpatterns = [
    path('request/',requestPage,name='deliveryRequest'),
    path('',homePage,name='homePage')
]