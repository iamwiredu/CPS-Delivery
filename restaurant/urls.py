from django.urls import path
from .views import restaurantHome


urlpatterns = [
    path('restaurant/home',restaurantHome.as_view(),name='restaurantHome'),
]