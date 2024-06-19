from django.urls import path
from .views import requestPage, homePage, pendingRequest, pastRequest, activeRequest, detailsPage, ShopPage, StoragePage

urlpatterns = [
    path('request/',requestPage,name='deliveryRequest'),
    path('',homePage,name='homePage'),
    path('pendingRequest/',pendingRequest,name='pendingRequest'),
    path('pastRequest/',pastRequest,name='pastRequest'),
    path('activeRequest/',activeRequest,name='activeRequest'),
    path('detailsPage/<str:unique_id>/',detailsPage,name='detailsPage'),
    path('shopPage/',ShopPage,name='ShopPage'),
    path('storage/',StoragePage,name='StoragePage'),
]