from django.test import TestCase, Client
from catalog.models import Product
from catalog.forms import ProductAddToCartForm
from .models import CartItem
import cart
from django.urls import reverse
from django.db import IntegrityError
from django.conf import settings
import httplib
import logging


 
class CartTestCase(TestCase):

	fixtures = ['catalog_data'] 


	def setUp(self):
		self.client = Client()
		self.product = Product.active.all()[0]



	def test_cart_id(self):
		home_url = reverse('catalog_home')
		self.client.get(home_url)
		#check that there is a cart id set in session after a page with cart box has been requested
		self.failUnless(self.client.session.get(cart.CART_ID_SESSION_KEY, ''))



	def test_add_product(self):
		QUANTITY = 2
		product_url = self.product.get_absolute_url()
		logging.error(product_url)
		response = self.client.get(product_url)
		self.assertEqual(response.status_code, httplib.OK)

		#store count in cart_count variable
		cart_item_count = self.get_cart_item_count()

		#assert cart cart item count is zero
		self.failUnlessEqual(cart_item_count, 0)

		#perform the post of adding to the cart
		context = {
					'product_slug': self.product.slug, 
					'quantity': QUANTITY,
					}
		response = self.client.post(product_url, context ) 

		#assert redirected to cart page - 302 then 200
		cart_url = reverse('show_cart')
		self.assertRedirects(response, cart_url, status_code=httplib.FOUND, target_status_code=httplib.OK )

		#assert cart item count is incremented by one
		self.assertEqual(self.get_cart_item_count(), cart_item_count + 1) #fail

		cart_id = self.get_cart_id()
		last_item = CartItem.objects.filter(cart_id=cart_id).latest('date_added')
		#assert the latest cart item has a quantity of two
		self.failUnlessEqual(last_item.quantity, QUANTITY)
		#assert the latest cart item is the correct product
		self.failUnlessEqual(last_item.product, self.product)



	def get_cart_item_count(self):
		cart_id = self.get_cart_id()
		return CartItem.objects.filter(cart_id=cart_id).count()



	def get_cart_id(self):
		return self.client.session.get(cart.CART_ID_SESSION_KEY)



 	def test_add_product_empty_quantity(self):
 		product_url = self.product.get_absolute_url()
 		postdata = {
 				   'product_slug': self.product.slug,
 				   'quantity': ''
 				   }
 		response = self.client.post(product_url, postdata )

 		expected_error = unicode(ProductAddToCartForm.base_fields['quantity'].error_messages['required'])
 		self.assertFormError(response, 'form', 'quantity', [expected_error]) # fail no context



 	def test_add_product_zero_quantity(self):
		product_url = self.product.get_absolute_url()
		postdata = {
					'product_slug': self.product.slug, 
					'quantity': 0 
					} 
		response = self.client.post(product_url, postdata )
		# need to concatenate the min_value onto error_text containing %s
		error_text = unicode(ProductAddToCartForm.base_fields['quantity'].error_messages['min_value'])
		min_value = ProductAddToCartForm.base_fields['quantity'].min_value 
		expected_error = error_text #% min_value
		self.assertFormError(response, "form", "quantity", [expected_error]) #fail no context



 	def test_add_product_invalid_quantity(self):
 		product_url = self.product.get_absolute_url()
 		postdata = {
 				   'product_slug': self.product.slug,
 				   'quantity': 'bg',
 				   }
 		response = self.client.post(product_url, postdata ) 
 		expected_error = unicode(ProductAddToCartForm.base_fields['quantity'].error_messages['invalid'])
 		self.assertFormError(response, 'form', 'quantity', [expected_error]) #fail no context




 	

 
















