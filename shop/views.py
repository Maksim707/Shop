from .models import Product
from django.shortcuts import render

def catalog(request):
	products = Product.objects.all()
	return render(request, 'shop/catalog.html', {'products': products})

def create_order(request):
	return render(request, 'shop/create_order.html')

def orders(request):
	return render(request, 'shop/orders.html')


# Create your views here.
