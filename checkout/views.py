from django.http import HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse
from .models import Order, OrderItem
import checkout
from cart import cart
from .forms import CheckoutForm
import logging
from accounts import profile 


# Create your views here.

def show_checkout(request):
	error_message = ''
	if cart.is_empty(request):
		cart_url = reverse('show_cart')
		return HttpResponseRedirect(cart_url)

	if request.method == 'POST':   
		postdata = request.POST.copy()
		form = CheckoutForm(postdata ) 
		order_number = request.session.get('order_number', '')

		if form.is_valid():  
			response = checkout.process(request)
			order_number = response.get('order_number', 0)
			error_message = response.get('message', '')
			if order_number:
				request.session['order_number'] = order_number
				receipt_url = reverse('checkout_receipt')
				return HttpResponseRedirect(receipt_url)
		else:
			error_message = 'Correct the errors below' 
	else:
		if request.user.is_authenticated:
			user_profile = profile.retrieve(request)
			form = CheckoutForm(instance=user_profile)
		else:
			form = CheckoutForm() 
	 
	page_title = 'Checkout'
	total = cart.cart_subtotal(request)
	template = 'checkout/checkout.html'
	context = {
			  'page_title': page_title,
			  'error_message': error_message,
			  'form': form,
			  'total': total,
			  }
	return render(request, template, context) 




def receipt(request):
	order_number = request.session.get('order_number', '')
	if order_number:
		order = Order.objects.filter(id=order_number)[0]
		order_items = OrderItem.objects.filter(order=order)

		del request.session['order_number']
	else:
		cart_url = reverse('show_cart')
		return HttpResponseRedirect(cart_url)
	template = 'checkout/receipt.html'
	context = {
			  'order_items': order_items,
			  'order': order,
			  }
	return render(request, template, context)














