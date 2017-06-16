from cart import cart
from .models import Order, OrderItem
from .forms import CheckoutForm
from django.conf import settings
from django.urls import reverse
import urllib
import stripe
import logging
from cart.models import CartItem


#return the url from the checkout module for the cart
def get_checkout_url(request):
	return reverse('checkout') 



def process(request):

	response = _charge_card(request) 

	results = {}  
	if response['status'] == 'succeeded':
		transaction_id = response['created'] 
		order = create_order(request, transaction_id)
		results = {'order_number': order.id, 'message':''}
	if response['status'] != 'succeeded':
		results = {'order_number': 0, 'message':'There is a problem with your credit card.'} #?
	if response['status'] == 'error':
		results = {'order_number': 0, 'message': 'Error processing your order.'} #?
	return results



def create_order(request, transaction_id):
	order = Order()
	checkout_form = CheckoutForm(request.POST, instance=order) 

	order = checkout_form.save(commit=False)  

	order.transaction_id = transaction_id
	order.ip_address = request.META.get('REMOTE_ADDR')

	order.user = None
	if request.user.is_authenticated:   
		order.user = request.user

	order.status = Order.SUBMITTED
	order.save()
	#if the order save succeeded
	if order.pk:

		cart_items = cart.get_cart_items(request)
		for ci in cart_items:
			#create order item for each cart item
			oi = OrderItem()
			oi.order = order
			oi.quantity = ci.quantity
			oi.price = ci.price #now using @property
			oi.product = ci.product
			oi.save()
		#all set, empty cart
		cart.empty_cart(request)
		#save profile info for future orders
		if request.user.is_authenticated:
			from accounts import profile
			profile.set(request) 
	#return the new order object
	return order 




def _charge_card(request):
	# Set your secret key: remember to change this to your live secret key in production
	# See your keys here: https://dashboard.stripe.com/account/apikeys
	stripe.api_key = "sk_test_WLxYShx8DyIsJkDKDAjQlpFU"

	# Token is created using Stripe.js or Checkout!
	# Get the payment token submitted by the form:

	token = request.POST['stripeToken']   

	
	amount = int(cart.cart_subtotal(request)*100)

	try:
		# Charge the user's card:
		charge = stripe.Charge.create(
		  	amount=amount,
		  	currency="usd",
		  	description="Example charge",
		  	source=token,
	)
	except stripe.error.CardError as e:
		# The card has been declined
		pass
		
	return charge


































