from django.urls import path
from .views import requestPage, homePage, pendingRequest, pastRequest,automaticLogout, OnlinePharmacy,activeRequest, detailsPage, ShopPage, StoragePage

urlpatterns = [
    path('request/',requestPage,name='deliveryRequest'),
    path('',homePage,name='homePage'),
    path('pendingRequest/',pendingRequest,name='pendingRequest'),
    path('pastRequest/',pastRequest,name='pastRequest'),
    path('activeRequest/',activeRequest,name='activeRequest'),
    path('detailsPage/<str:unique_id>/',detailsPage,name='detailsPage'),
    path('shopPage/',ShopPage,name='ShopPage'),
    path('storage/',StoragePage,name='StoragePage'),
    path('onlinePharmacy/',OnlinePharmacy,name='OnlinePharmacy'),
    path('automatic/logout/',automaticLogout,name='automaticLogout')
]