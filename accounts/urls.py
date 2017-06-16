from django.conf.urls import *
from django.conf import settings
from .views import register, my_account, order_details, order_info
from django.contrib.auth import views as auth_views




urlpatterns = [
	
	url(r'^register/$', register, name='register'),
	url(r'^my_account/$', my_account, name='my_account'),
	url(r'^order_details/(?P<order_id>[-\w]+)/$', order_details, name='order_details'),
	url(r'order_info/$', order_info, name='order_info'),
	
	

]


urlpatterns += [

	url(r'^login/$', auth_views.login, name='login'),

	url(r'^logout/$', auth_views.logout, name='logout'),

	url(r'^password_change/$', auth_views.password_change, name='password_change'), 
	
]








