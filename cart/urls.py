from django.conf.urls  import *
from .views import show_cart




urlpatterns = [
	url(r'^$', show_cart, name='show_cart')

]


