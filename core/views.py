from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse

from core.forms import OrderForm
from core.models import Product,Size,Order,OrderItem

import random
import json


def home(request):
	return render(request, "home.html")

def menu(request):
	return render(request,"menu.html", {'products': Product.objects.all()})

def checkout(request):
	if request.method == "POST":
		f = OrderForm(request.POST)
		if f.is_valid():
			o = f.save()
			total = 0
			for i in json.loads(request.POST.get("data"))['data']:
				p = Product.objects.filter(pk = int(i['p']))[0]
				s = Size.objects.filter(pk = int(i['s']))[0]
				OrderItem.objects.create(order = o,name = p.name,price = s.price,size_name = s.name,quantity = int(i['q']))
				total += s.price*int(i['q'])
			o.order_id = ''.join(random.choices("0123456789",k = 6))
			o.total = total
			o.save()
			return redirect("core:thank_you",number = o.order_id)
	return render(request,"checkout.html")

def product(request, pk):
	product = get_object_or_404(Product, pk=pk)
	pizzas = Product.objects.filter(catagory='Pizzas')[:3]
	sizes = Size.objects.filter(product=product)
	return render(request,"product.html",{'product': product,'pizzas': pizzas,'sizes': sizes})

def thank_you(request, number):
	return render(request, "thankyou.html", {'number': number})

def track_order(request):
	return render(request, "track_order.html")

def track_order_num(request, number):
	order = Order.objects.filter(order_id=number)
	if order:
		return JsonResponse({"message":f"Hello {order[0].name}! Your Order Status is : {order[0].state}"})
	return JsonResponse({"message":f"Order Not Found!"})
