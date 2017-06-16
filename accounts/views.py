from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.urls import reverse
from django.http import HttpResponseRedirect
from checkout.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
import profile
import logging


# Create your views here.
def register(request):
	if request.method == 'POST':
		postdata = request.POST.copy()
		form = UserCreationForm(postdata)
		if form.is_valid():
			form.save()
			un = postdata.get('username', '')
			pw = postdata.get('password1', '')
			from django.contrib.auth import login, authenticate
			new_user = authenticate(username=un, password=pw)
			if new_user and new_user.is_active:
				login(request, new_user)
				url = reverse('my_account')
				return HttpResponseRedirect(url) 
	else:
		form = UserCreationForm()
	page_title = 'User Registration'
	template = 'registration/register.html'
	context = {
			  'form':form,
			  'page_title':page_title,
			  }
	return render(request, template, context) 





@login_required
def my_account(request):
	page_title = 'My Account'
	orders = Order.objects.filter(user=request.user)
	name = request.user.username
	template = 'registration/my_account.html'
	context = {
			  'page_title': page_title,
			  'orders': orders,
			  'name': name
			  }
	return render(request, template, context) 




@login_required
def order_details(request, order_id):
	#if order id does not match the user, will return a 404 error 
	order = get_object_or_404(Order, id=order_id, user=request.user)
	page_title = 'Order Details for Order #' + order_id
	order_items = OrderItem.objects.filter(order=order)
	template = 'registration/order_details.html'
	context = {
			  'page_title': page_title,
			  'order': order,
			  'order_items': order_items,
		      }
	return render(request, template, context)




def order_info(request):
	
	if request.method == 'POST':
		postdata = request.POST.copy()
		form = UserProfileForm(postdata)
		if form.is_valid():
			profile.set(request)
			url = reverse('my_account')
			return HttpResponseRedirect(url)
	else:
		user_profile = profile.retrieve(request)
		form = UserProfileForm(instance=user_profile) 
	page_title = 'Edit Order Information'
	template = 'registration/order_info.html'
	context = {
			  'page_tile': page_title,
			  'form': form,
			  }
	return render(request, template, context)

	























