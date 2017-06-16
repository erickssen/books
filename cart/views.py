from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
import cart
import logging
from checkout import checkout
 	



def show_cart(request):
	template = 'cart/cart.html'

	if request.method == 'POST':
		postdata = request.POST.copy()
		
		if 'remove' in postdata:
			cart.remove_from_cart(request) 

		if 'update' in postdata:
			cart.update_cart(request) 

		if 'Checkout' in postdata:
			checkout_url = checkout.get_checkout_url(request)
			return HttpResponseRedirect(checkout_url)
	
	cart_items = cart.get_cart_items(request)
	page_title = 'Shopping Cart'
	cart_subtotal = cart.cart_subtotal(request)
	
	context = {
			  'cart_items': cart_items,
			  'page_title': page_title,
			  'cart_subtotal': cart_subtotal,
			  }
	return render(request, template, context) 



 





