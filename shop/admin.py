from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','price','discount','rating','stock','is_avaliable','desc','img','likes')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id','product', 'delivery_address', 'created_at')
