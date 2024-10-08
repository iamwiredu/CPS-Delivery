from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from home.models import Profile
from .models import Restaurant, Food
from .forms import RestaurantForm, FoodForm
from django.contrib.auth.decorators import login_required
from .models import  Food
from delivery.models import CartRestaurant, Side,CartItemRestaurant, RestaurantOrder, DeliveryRequest
# Create your views here.

class restaurantHome(View):

    def get(self,request):
        restaurants = Restaurant.objects.all()
        context ={
            'restaurants':restaurants,
        }
        return render(request,'html/restaurantHome.html',context)
    

class restaurantSignUp(View):

    def get(self,request):
        return render(request,'html/restaurantSignUp.html')
    
    def post(self, request):

        if 'addUser' in request.POST:
            try:
                username = request.POST.get('username')
                password = request.POST.get('password1')
                email = request.POST.get('email')
                first_name = request.POST.get('fname')
                last_name = request.POST.get('lname')
                phone = request.POST.get('phone')

                # restaurant details
                rname = request.POST.get('rname')
                raddress = request.POST.get('raddress')
                rdescription = request.POST.get('rdescription')
                rhours = request.POST.get('rhours')
                rimage = request.FILES.get('rimage')
                # Create the user
                user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                
                # Set the password correctly
                user.set_password(password)
                user.save()

                # create a restaurant for user
                restaurant, created = Restaurant.objects.get_or_create(user=user)

                restaurant.user = user
                restaurant.name = rname
                restaurant.address = raddress
                restaurant.description = rdescription
                restaurant.opening_hours = rhours
                restaurant.image = rimage
                print(restaurant)

                restaurant.save()


                # Create or get the user's profile
                profile, created = Profile.objects.get_or_create(user=user)
                profile.restaurant = restaurant
                profile.user = user
                profile.phone = phone  # Assuming `Profile` has a `phone` field
                profile.accountType = 'Restaurant'
                profile.save()

     


            except Exception as e:
                print(e)
            return redirect('/login/')
        
class restaurantAdmin(View):
    

    def get(self,request):
        restaurant = Restaurant.objects.get(user=request.user)
        context ={
            'restaurant':restaurant,
            
        }
        return render(request,'html/restaurantAdmin.html',context)
    
class restaurantUpdate(View):

    def get(self,request,unique_id):
        try:
            restaurant = Restaurant.objects.get(unique_id=unique_id)
        except Restaurant.DoesNotExist:
            return HttpResponse('<h1>Object does not exist.</h1>')
        
        restaurantForm = RestaurantForm(instance=restaurant)
        context ={
            'restaurant':restaurant,
            'restaurantForm': restaurantForm,
        }
        
        
        return render(request,'html/restaurantUpdate.html',context)
    
    def post(self,request,unique_id):
        restaurant = Restaurant.objects.get(unique_id=unique_id)
        if 'updateRestaurant' in request.POST:
            restaurantObj  = RestaurantForm(request.POST,request.FILES,instance=restaurant)
            if restaurantObj.is_valid():
                restaurantObj.save()
                return redirect('/restaurantAdmin/')
            else:
                print('error') # handle error message well


class restaurantFood(View):
    foodFormCreator = FoodForm()

    def get(self,request,unique_id):
        try:
            restaurant = Restaurant.objects.get(unique_id=unique_id)
        except Restaurant.DoesNotExist:
            return HttpResponse('<h1>Object does not exist.</h1>')
        
        foods = Food.objects.all().filter(restaurant=restaurant)
        
        context = {
            'restaurant':restaurant,
            'foods':foods,
            'foodFormCreator':self.foodFormCreator,
        }
        return render(request,'html/restaurantFood.html',context)
    def post(self,request,unique_id):
        restaurant = Restaurant.objects.get(unique_id=unique_id)
        if 'addFood' in request.POST:
            food = FoodForm(request.POST, request.FILES)
            if food.is_valid():
                event = food.save(commit=False)
                event.restaurant = restaurant
                event.save()

                return redirect(f'/restaurantFood/{unique_id}')
            else:
                print('error')
        if 'addSide' in request.POST:
            food = request.POST.get('food')
            name = request.POST.get('name')
            food = Food.objects.get(unique_id=food)
            side = Side(food=food,name=name)
            side.save()

            return redirect(f'/restaurantFood/{unique_id}')


class restaurantOrder(View):
    
    def get(self,request,unique_id):
        restaurant = Restaurant.objects.get(unique_id=unique_id)
        foods = Food.objects.all().filter(restaurant=restaurant)
        context = {
            'foods':foods,
            'restaurant':restaurant,
        }
        return render(request,'html/restaurantOrder.html',context)
    
    def post(self,request,unique_id):
        if 'addToCart' in request.POST:
            print('yes')
            restaurant = Restaurant.objects.get(unique_id=unique_id)
            food_id = request.POST.get('food_uniqueId')
            quantity = request.POST.get('quantity')
            
            food = Food.objects.get(unique_id=food_id)
            cart, created = CartRestaurant.objects.get_or_create(user=request.user,completed=False,restaurant=restaurant)
            cartItem,created = CartItemRestaurant.objects.get_or_create(cart=cart,food=food)

            cartItem.quantity = int(quantity)
            cartItem.save()

            return redirect(f'/restaurantOrder/{unique_id}')


    


@login_required
def add_to_cart(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    cart, created = CartRestaurant.objects.get_or_create(user=request.user)

    cart_item, item_created = CartItemRestaurant.objects.get_or_create(cart=cart, food=food)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')  # Redirect to the cart view page



# View for displaying the cart
@login_required
def cart_view(request,unique_id):
    restaurant = Restaurant.objects.get(unique_id=unique_id)
    cart, created = CartRestaurant.objects.get_or_create(user=request.user,completed=False,restaurant=restaurant)
    cart_items = cart.cart_items.all()
    total_price = cart.total_price

    if request.method == 'POST':     
        if 'remove' in request.POST:
            cart_id = request.POST.get('cartId')
        
            cart_item = get_object_or_404(CartItemRestaurant, unique_id=cart_id)
       
            cart_item.delete()


            return redirect('/cart/')
        if 'update' in request.POST:
            cart_id = request.POST.get('cartIdUpdate')
            quantity = request.POST.get('quantity')
        
            cart_item = get_object_or_404(CartItemRestaurant, unique_id=cart_id)
            cart_item.quantity = quantity
            cart_item.save()
            return redirect('/cart/')
        
        if 'placeOrder' in request.POST:
            try:

                Location = request.POST.get('Location')
                Phone = request.POST.get('phone')
                # create restaurant order
                restaurant_order = RestaurantOrder(restaurant=restaurant,Cart=cart)
                restaurant_order.save()

                # set cart to complete
                cart.completed = True
                cart.save()

                # create single request
                delivery_request = DeliveryRequest(user=request.user)
                delivery_request.orderQuantity = len(cart.cart_items.all())
                delivery_request.pickupNumber = restaurant.user.profile.phone
                delivery_request.deliveryPoint = 'Kumasi'
                delivery_request.dropoffLocation = Location
                delivery_request.dropoffNumber = Phone
                delivery_request.pickupPoint = 'Kumasi'
                delivery_request.pickupLocation = restaurant.address
                delivery_request.productFee = cart.total_price

                delivery_request.save()

                return redirect(cart_view,unique_id)
            except Exception as e:
                print(e)
            
    return render(request, 'cart/cartRestaurant.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart':cart,
    })
