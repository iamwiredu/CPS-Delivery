from django.shortcuts import render
from django.views import View

# Create your views here.

class restaurantHome(View):

    def get(self,request):
        return render(request,'html/restaurantHome.html')