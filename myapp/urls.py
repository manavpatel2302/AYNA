from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [

    path('feedback', views.feedback, name='feedback'),
    path('fertilizer', views.fertilizer, name='fertilizer'),
    path('govts', views.govts, name='govts'),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('seed_price', views.seed_price, name='seed_price'),
    path('seed', views.seed, name='seed'),
    path('solarpanel', views.solarpanel_view, name='solarpanel'),

    path('tech', views.modern_view, name='tech'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('confirm_password',views.confirm_password,name='confirm_password'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),
    path('get-weather/', views.get_weather, name='get_weather'),
    path('weather', views.weather, name='weather'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-to-cart/<int:seed_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-quantity/<int:cart_item_id>/', views.update_quantity, name='update_quantity'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment-success/', views.payment_success, name='payment_success'),


]
 



