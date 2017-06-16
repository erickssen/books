from django.test import TestCase, Client
from django.urls import reverse
from .forms import CheckoutForm
from .models import Order, OrderItem
from catalog.models import Category, Product
from cart import cart
from cart.models import CartItem
import httplib




class CheckoutTestCase(TestCase):

	fixtures = ['initial_data.json']

	def setUp(self):
		self.client = Client()
		home_url = reverse('catalog_home')
		self.checkout_url = reverse('checkout')
		self.client.get(home_url)
		#create a customer with a shopping cart
		self.item = CartItem()
		product = Product.active.all()[0]
		self.item.product = product
		self.item.cart_id = self.client.session.get(cart.CART_ID_SESSION_KEY, '')
		self.item.quantity = 1
		self.item.save()



	def test_checkout_page_empty_cart(self):
		'''empty cart should be redirected to cart page'''
		client = Client()
		cart_url = reverse('show_cart')
		response = client.get(self.checkout_url)
		self.assertRedirects(response, cart_url)


	def test_submit_empty_form(self):
		'''empty form should raise error on requiered fields'''
		form = CheckoutForm()
		response = self.client.post(self.checkout_url, form.initial) 
		for name, field in form.fields.iteritems():
			value = form.fields[name]
			if not value and form.fields[name].required:
				error_msg = form.fields[name].error_messages['required']
				self.assertFormError(response, 'form', name, [error_msg]) 


























