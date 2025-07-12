from django.contrib import admin
from myapp.models import *


# Register your models here.

admin.site.register(data)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')


from django.contrib import admin
from .models import Seed

@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(CartItem)
admin.site.register(coupon)

from django.contrib import admin
from .models import SolarPanelContent

@admin.register(SolarPanelContent)
class SolarPanelContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

@admin.register(modernday_tech)
class modernday_tech(admin.ModelAdmin):
    list_display = ('title', 'link')