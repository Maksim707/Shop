from .models import Product, Order
from django.shortcuts import render, redirect

def catalog(request):
	products = Product.objects.all()
	return render(request, 'shop/catalog.html', {'products': products})

def create_order(request, id):
	if request.method =='POST':
		print(request.POST['delivery_address'])
		Order.objects.create(
			product_id = id,
			delivery_address= request.POST['delivery_address'], 
		)
		return redirect('orders')
	return render(request, 'shop/create_order.html', {'product': Product.objects.get(id=id)})


def orders(request):
	orders = Order.objects.all()
	return render(request, 'shop/orders.html', {'orders': orders})

def product_detail(request, id):
	return render(request, 'shop/product_detail.html', {'product': Product.objects.get(id=id)})
