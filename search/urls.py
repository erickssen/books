from django.conf.urls import *
import views




urlpatterns = [

	url(r'^results/$', views.results, name='search_results'), 


]

