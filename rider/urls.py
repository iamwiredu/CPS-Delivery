from django.urls import path
from .views import riderManagement

urlpatterns = [
    path('rider/management/<str:unique_id>/',riderManagement,name="riderManagement")
]