from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import SESSION_KEY
from django.contrib.auth.models import User 
from catalog.models import Category, Product, ProductReview
import httplib
from decimal import Decimal
from django.db import IntegrityError
from django.conf.urls import handler404 




# Create your tests here.


class NewUserTestCase(TestCase):

	fixtures = ['initial_data'] 

	def setUp(self):
		self.client = Client()
		logged_in = self.client.session.has_key(SESSION_KEY)
		self.assertFalse(logged_in)


	def test_view_homepage(self):
		home_url = reverse('catalog_home')
		response = self.client.get(home_url)
		#check if we got a response
		self.failUnless(response)
		#check that status code of response was 'httplib.ok = 200'
		self.assertEqual(response.status_code, httplib.OK) 


 	def test_view_category(self):
 		category = Category.active.all()[0]
 		category_url = category.get_absolute_url()
 		#test loading of catagory page
 		response = self.client.get(category_url)
 		self.failUnless(response)
 		self.assertEqual(response.status_code, httplib.OK)
 		#test that the category.html template is in the response
 		self.assertTemplateUsed(response, 'catalog/category.html') 
 		# test that category page contains category information
 		self.assertContains(response, category.name)
 		self.assertContains(response, category.description) 


 	def test_view_product(self):
 		'''test product view loads'''
 		product = Product.active.all()[0]
 		product_url = product.get_absolute_url()
 		response = self.client.get(product_url)
 		self.failUnless(response)
 		self.assertEqual(response.status_code, httplib.OK)
 		self.assertTemplateUsed('category/product.html')
 		self.assertContains(response, product.name)
 		self.assertContains(response, product.description) 



class ActiveProductManagerTestCase(TestCase):

	fixtures = ['initial_data']

	def setUp(self):
		self.client = Client()

	def test_inactive_product_returns_404(self):
		#product in fixture file is set to: is_active=False
		product = Product.objects.filter(is_active=False)[0]
		product_url = product.get_absolute_url()
		# django_404_template = handler404
		response = self.client.get(product_url)
		# self.assertTemplateUsed(response, django_404_template)
		self.assertTemplateNotUsed(response, 'category/product.html') 




class ProductTestCase(TestCase):

	fixtures = ['initial_data'] 

	def setUp(self):
		self.product = Product.active.all()[0]
		self.product.price = Decimal('199.99')
		self.product.save()
		self.client = Client()



	def test_sale_price(self):
		self.product.old_price = Decimal('220.00')
		self.product.save()
		self.failIfEqual(self.product.sale_price, None)
		self.assertEqual(self.product.sale_price, self.product.price)



	def test_no_sale_price(self):
		self.product.old_price = Decimal('0.00')
		self.product.save()
		self.failUnlessEqual(self.product.sale_price, None)



	def test_permalink(self):
		url = self.product.get_absolute_url()
		response = self.client.get(url)
		self.failUnless(response)
		self.assertEqual(response.status_code, httplib.OK)


	def test_unicode(self):
		self.assertEqual(self.product.__unicode__(), self.product.name) 



class ProductReviewCase(TestCase):

	fixtures = ['initial_data', ] 

	#test if models can be saved without foreign keys
	def test_orphaned_product_review(self):
		pr = ProductReview()
		self.assertRaises(IntegrityError, pr.save) 


	#test that fields with defaults fall back to the provided default
	def test_product_review_defaults(self):
		user = User.objects.all()[0]
		product = Product.active.all()[0]
		pr = ProductReview(user=user, product=product)
		pr.save()
		for field in pr._meta.fields:
			if field.has_default():
				self.assertEqual(pr.__dict__[field.name], field.default)














