from django.urls import path
from .views import requestPage, homePage, pendingRequest, pastRequest, activeRequest

urlpatterns = [
    path('request/',requestPage,name='deliveryRequest'),
    path('',homePage,name='homePage'),
    path('pendingRequest/',pendingRequest,name='pendingRequest'),
    path('pastRequest/',pastRequest,name='pastRequest'),
    path('activeRequest/',activeRequest,name='activeRequest')
]