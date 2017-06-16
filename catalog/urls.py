from django.conf.urls import url
from django.contrib import admin




from .views import(
	index,
	show_category,
	show_product,
	add_review,
	add_tag,
	tag_cloud,
	tag,
	 
)



urlpatterns = [
	url(r'^$', index, name='catalog_home'),
	url(r'^category/(?P<category_slug>[-\w]+)/$', show_category, name='catalog_category'),
	url(r'^product/(?P<product_slug>[-\w]+)/$', show_product, name='catalog_product'),
	url(r'^review/product/add/$', add_review ), 
	url(r'^tag/product/add/$', add_tag ),
	url(r'^tag_cloud/$', tag_cloud, name='tag_cloud'), 
	url(r'^tag/(?P<tag>[-\w]+)/$', tag, name='tag'), 
	     
]




