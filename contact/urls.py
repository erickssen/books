from django.conf.urls import url
from .views import contact_us




urlpatterns = [
	url(r'^contact_us/$', contact_us, name='contact_us'), 


]


