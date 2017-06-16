from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, Template
from .models import Category, Product, ProductReview 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from cart import cart 
from catalog.forms import ProductAddToCartForm
from catalog.forms import ProductReviewForm
from stats import stats
from django.conf import settings 
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT
import json 
import logging
import tagging
from tagging.models import Tag, TaggedItem 
from django.views.decorators.cache import cache_page


 

def index(request):
	search_recs = stats.recommended_from_search(request)

	featured= Product.featured.all()[ 0:settings.PRODUCTS_PER_ROW ]  
	recently_viewed = stats.get_recently_viewed(request)
	view_recs = stats.recommended_from_views(request) 

	page_title = 'books'
	template = 'catalog/index.html'
	context = {
			   'page_title': page_title,
			   'search_recs':search_recs,
			   'view_recs': view_recs,
			   'featured': featured,
			   'recently_viewed': recently_viewed,   
			  }
	return render(request, template, context) 



# @cache_page(60 * 60)
def show_category(request, category_slug):
	category_cache_key = request.path
	c = cache.get(category_cache_key)
	if not c:
		c = get_object_or_404(Category, slug=category_slug) 
		cache.set(category_cache_key, c, CACHE_TIMEOUT)

	products = c.product_set.all()
	page_title = c.name
	meta_keywords = c.meta_keywords
	meta_description = c.meta_description
	
	template = 'catalog/category.html'
	
	context = {
			   'c':c,
			   'products': products, 
			   'page_title': page_title,
			   'meta_keywords': meta_keywords,
			   'meta_description': meta_description
			   } 	
	return render(request, template, context)




def show_product(request, product_slug):
	#cache key is product  path
	product_cache_key = request.path
	p = cache.get(product_cache_key)
	# if cache miss, fall back on database query
	if not p:
		p = get_object_or_404(Product.active, slug=product_slug)
		#store in cache for next time
		cache.set(product_cache_key, p, CACHE_TIMEOUT) 

	categories = p.categories.filter(is_active=True)
	page_title = p.name
	meta_keywords = p.meta_keywords
	meta_description = p.meta_description
	product_reviews = ProductReview.approved.filter(product=p).order_by('-date')
	review_form = ProductReviewForm() 
	 
	template = 'catalog/product.html'
	
	if request.method == 'POST':
		postdata = request.POST
		form = ProductAddToCartForm(request, postdata) 
		
		if form.is_valid():
			#add to cart and redirect to cart page
			cart.add_to_cart(request)

		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
		url = reverse('show_cart')
		return HttpResponseRedirect(url)
	else:
		#it's a GET, create the unbound form.  Note request as a kward
		form = ProductAddToCartForm(request=request, label_suffix=':')
		#assign the hidden imput the product slug
		form.fields['product_slug'].widget.attrs['value'] = product_slug
		#set the test cookie on first GET request
		request.session.set_test_cookie()

	context =  {
				'p': p,
				'categories': categories,
				'page_title': page_title,
				'meta_keywords': meta_keywords,
				'meta_description': meta_description,
				'form': form,
				'product_reviews': product_reviews,
				'review_form': review_form,
				} 
	#log product in ProductView to recomend and get recently view products (this should be done using Django middleware class) 
	x = stats.log_product_views(request, p) 
	return render(request, template, context) 




#reviews
@csrf_exempt
@login_required
def add_review(request):
	form = ProductReviewForm(request.POST)
	if form.is_valid():
		review = form.save(commit=False)
		slug = request.POST.get('slug')
		product = Product.active.get(slug=slug)
		review.user = request.user
		review.product = product
		review.save()

		template = "catalog/product_review.html"
		html = render_to_string(template, {'review': review }) 
		response = json.dumps({'success':'True', 'html':html })
	else:
		html = form.errors.as_ul()
		response = json.dumps({'success':'False', 'html':html }) 
	#send back to the jQuery 
	return HttpResponse(response, content_type='application/javascript; charset=utf-8') 



#tagging 
@csrf_exempt 
@login_required
def add_tag(request):
	tags = request.POST.get('tag','')
	slug = request.POST.get('slug','')
	if len(tags) > 2:
		p = Product.active.get(slug=slug)
		html = u''
		template = 'catalog/tag_link.html'
		for tag in tags.split():
			tag.strip(',')
			Tag.objects.add_tag(p, tag)
		for tag in p.tags:
			html += render_to_string(template, {'tag': tag })
		response = json.dumps({'success':'True', 'html':html }) 
	else:
		response = json.dumps({'success': 'False'}) 
	return HttpResponse(response, content_type='application/javascript; charset=utf-8') 
 




def tag_cloud(request):
	product_tags = Tag.objects.cloud_for_model(Product, steps=9, distribution=tagging.utils.LOGARITHMIC, filters={'is_active': True })
	page_title = 'Product Tag Cloud'
	template = 'catalog/tag_cloud.html'
	context = {
			  'product_tags':product_tags,
			  'page_title':page_title,
			  }
	return render(request, template, context)




def tag(request, tag):
	products = TaggedItem.objects.get_by_model(Product.active, tag)
	template = 'catalog/tag.html'
	context = {
			  'products':products,
			  'tag':tag,
			  }
	return render(request, template, context) 







  






	
