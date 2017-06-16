from django.conf.urls import *
from django.conf import settings
from .views import show_checkout, receipt 


urlpatterns = [

	url(r'^$', show_checkout, name='checkout'),

	url(r'^receipt/$', receipt, name='checkout_receipt'),


]



