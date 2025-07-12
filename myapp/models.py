from django.db import models

# Create your models here.

class data(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.IntegerField()
    confirm_password=models.IntegerField()
    otp=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.username


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Feedback from {self.name} - {self.email}"

# models.py
from django.db import models

class Seed(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='seed_images/')
    wikipedia_link = models.URLField()  # New field for Wikipedia link

    def __str__(self):
        return self.name


# models.py
class CartItem(models.Model):
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.seed.price * self.quantity

    def __str__(self):
        return f"{self.seed.name} - {self.quantity} pcs"



class coupon(models.Model):
        coupon_name=models.CharField(max_length=20)
        discount=models.IntegerField()

     
        def __str__(self):
                return self.coupon_name
        
class user_coupon(models.Model):
    user=models.ForeignKey(data,on_delete=models.CASCADE)
    coupon=models.ForeignKey(coupon,on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the built-in User model




from django.db import models

class SolarPanelContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='solar_images/', null=True, blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

from django.db import models

class modernday_tech(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='solar_images/', null=True, blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title