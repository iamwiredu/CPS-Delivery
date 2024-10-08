from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .models import Profile
from .forms import ProfileForm
from rider.views import riderManagement
from restaurant.views import restaurantAdmin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class Home(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        return render(request,'home.html')

class Login(View):

    def get(self, request):
        context = {

        }
        return render(request, 'login.html', context)

    def post(self, request):
        if 'login' in request.POST:
            user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if user is not None:
                login(request,user)
                print('yes')
                if user.is_superuser:
                    return redirect('/adminConsole/')
                elif user.profile.accountType == 'Rider':
                    return redirect(riderManagement,request.user.profile.rider.unique_id) # associate every rider profile with a rider object
                elif user.profile.accountType == 'Restaurant':
                    return redirect('/restaurantAdmin/')
                else:
                    print(user.profile.accountType)
                    return redirect('/accounthome/')
                   
            
            else:
                messages.error(request,'Wrong Password or Username.')
                return redirect('/login/')

        context = {
        }
        return render(request, 'home.html', context)
        
class SignUp(View):

    def get(self,request):
        return render(request,'signUp.html')
    
    def post(self, request):

        if 'addUser' in request.POST:
            try:
                username = request.POST.get('username')
                password = request.POST.get('password1')
                email = request.POST.get('email')
                first_name = request.POST.get('fname')
                last_name = request.POST.get('lname')
                phone = request.POST.get('phone')

                # Create the user
                user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                
                # Set the password correctly
                user.set_password(password)
                user.save()

                # Create or get the user's profile
                profile, created = Profile.objects.get_or_create(user=user)
                profile.user = user
                profile.phone = phone  # Assuming `Profile` has a `phone` field
                profile.accountType = 'Nuser'
                profile.save()
            except:
                print('error')
            return redirect('/login/')


def custom_404(request, exception):
    return render(request, '404.html', status=404)