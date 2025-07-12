

from django.shortcuts import render,HttpResponse,redirect
from myapp.models import *
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def register(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']  
        print(username,email,password,confirm_password)  
        uid = data.objects.filter(email=email).exists()
        if uid:
            contaxt={
                "message":"Email is already exists." 
            }
        
            return render(request,"register.html",contaxt)
        else:
            if password == confirm_password:
                data.objects.create(username=username,email=email,password=password,confirm_password=confirm_password)
                return redirect(index)
            else:
                contaxt={
                "message":"Enter a valid password" 
            }
        
            return render(request,"register.html",contaxt)
    else:
        print("invalid data ")
        return render(request,"register.html")

# ----------------------------------------------------------------------------------------

def login(request):
    if "email" in  request.session:
        return redirect(index)
    else:
        if request.POST:
            email=request.POST["email"]
            password=request.POST["password"]       
            uid=data.objects.filter(email=email).exists()

            if uid:
                uid=data.objects.get(email=email)
                if password==str(uid.password):
                    request.session['email']=email
                    return redirect(index)
                else:
                    contaxt={
                        "msg":"invalide password",
                    }
                    return render(request,"login.html",contaxt)
            else:
                print(email,password)
                return render(request,"login.html")    
        else:  
            return render(request,"login.html")

# ----------------------------------------------------------------------------------------------

def logout(request):
    del request.session['email']
    return redirect(login)

# ==================================================================
import random
 
def forgot_password(request):
        if request.POST:
                email=request.POST["email"]  
                uid=data.objects.filter(email=email).exists()
                otp=random.randint(100000,999999)
                print(otp)
                if uid:
                     uid=data.objects.get(email=email)
                     uid.otp=otp
                     uid.save()
                     send_mail("Team AYNA",f"Your OTP is - {otp}","gohiljayb10@gmail.com", [email])
                     contaxt={
                         "uid":uid
                     }
                     return render(request,"con_password.html",contaxt)
                else:
                    contaxt={
                    "uid":uid,
                    "message":"invalid email"
                    }

                    return render(request,"forgot_password.html",contaxt)
        return render(request,"forgot_password.html")

def confirm_password(request):
    if request.POST:
        email=request.POST["email"]  
        otp=request.POST["otp"]  
        password=request.POST["password"]  
        confirm_password=request.POST["confirm_password"]  
        uid=data.objects.get(email=email)
        if uid.otp == int(otp):
            if password == confirm_password:
                uid.password=password
                uid.confirm_password=confirm_password
                uid.save()
                return redirect(login)
            else:
                contaxt={
                    "msg":"Invalid Password",
                    "uid":uid
                }
                return render(request,"con_password.html",contaxt)
        else:
            contaxt={
                "msg":"Invalid Otp",
                "uid":uid
            }
            return render(request,"con_password.html",contaxt)


    return render(request,"con_password.html")
# =========================================================================================





def feedback(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save data to the Feedback model
        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()

        
        # Clear the form or redirect
    return render(request, 'feedback.html')




def feedback_success(request):
    return render(request, 'feedback_success.html')


def fertilizer(request):
     return render (request,"fertilizer.html")

def govts(request):
     return render (request,"govts.html")

def index(request):
     return render (request,"index.html")



def seed_price(request):
    seeds = Seed.objects.all()
    return render(request, 'seed_price.html', {'seeds': seeds})


def seed(request):
     return render (request,"seed.html")

def solarpanel_view(request):
    content_list = SolarPanelContent.objects.all()
    return render(request, 'solarpanel.html', {'content_list': content_list})



def modern_view(request):
    content_list = modernday_tech.objects.all()
    return render(request, 'tech.html', {'content_list': content_list})

def weather(request):
     return render (request,"weather.html")

import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'London')
        print(f"City requested: {city}")

        api_key = '9bc1a53fff1aab790ae1770f9ef1b82b'  # ✅ Your working API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        print(f"URL used: {url}")

        response = requests.get(url)
        data = response.json()
        print(f"API Response: {data}")

        if data.get('cod') != 200:
            return JsonResponse({'error': data.get('message', 'City not found')}, status=404)

        weather = {
            'city': city,
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],  # ✅ Include the weather icon code
        }
        return JsonResponse(weather)

    return JsonResponse({'error': 'Invalid request'}, status=400)


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Seed, CartItem



def update_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))
        cart_item.quantity = new_quantity
        cart_item.save()
    return redirect('cart_view')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart_view')


def cart_view(request):
    
    cart_items = CartItem.objects.all()
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, seed_id):
    seed = Seed.objects.get(id=seed_id)
    
    # Check if the seed is already in the cart, if so update the quantity
    cart_item = CartItem.objects.create(seed=seed)
    

    return redirect('cart_view')



def coupon_view(request):
    cuid = data.objects.get(email=request.session['email'])

    print(cuid)
    if request.POST:
        coupon_name = request.POST['coupon_name']
        uid = coupon.objects.filter(coupon_name=coupon_name).exists()
        
        if uid:
            cid = coupon.objects.get(coupon_name=coupon_name)

            ucid = user_coupon.objects.filter(coupon=cid, user=cuid).exists()
            if ucid:
                messages.success(request, "already apply")
                return redirect(cart_view)
            else:
                user_coupon.objects.create(coupon=cid, user=cuid,status=True)
            return redirect(cart_view)
        
        else:
            context = {
                "msg": "invalid coupon"
            }
            return render(request, "cart.html", context)


import razorpay
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render
from .models import CartItem, coupon

# Razorpay credentials
RAZORPAY_KEY_ID = 'rzp_test_bilBagOBVTi4lE'
RAZORPAY_KEY_SECRET = '77yKq3N9Wul97JVQcjtIVB5z'

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

def checkout(request):
    cart_items = CartItem.objects.all()
    subtotal = sum(item.total_price() for item in cart_items)
    discount_amount = Decimal(0)
    applied_coupon = None

    if request.method == 'POST':
        code = request.POST.get('coupon_code')
        try:
            applied_coupon = coupon.objects.get(coupon_name=code)
            discount_amount = (Decimal(applied_coupon.discount) / 100) * subtotal
        except coupon.DoesNotExist:
            applied_coupon = None

    total = subtotal - discount_amount
    amount_paise = int(total * 100)  # Razorpay expects amount in paise

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    amount = 50000  # amount in paise = Rs 500
    currency = 'INR'
    payment = client.order.create({
        "amount": amount,
        "currency": currency,
        "payment_capture": '1'
    })


    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'discount_amount': discount_amount,
        'total': total,
        'applied_coupon': applied_coupon,
        'amount': amount,
        'api_key': settings.RAZORPAY_KEY_ID,
        'order_id': payment['id'],
        'amount_paise':amount_paise 

    }
    return render(request, 'checkout.html', context)


def payment_success(request):
    return render(request, 'seed_price.html')





