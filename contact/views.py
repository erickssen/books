from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings
import logging



def contact_us(request):
 	page_title = 'Contact us'
 	form = contactForm(request.POST or None) 
 	confirm_message = None

 	if form.is_valid():
 		#get attribute values from cleaned_data dict
 		name = form.cleaned_data['name']
 		comment = form.cleaned_data['comment']
 		subject = 'message from bookstore.com'
 		title = 'Thanks'
 		confirm_message = 'Message Sent'
 		message = '{} {}'.format(comment, name)
 		emailFrom = form.cleaned_data['email']
 		emailTo = [settings.EMAIL_HOST_USER]
 		form = None
 		send_mail(
 			subject,
 			message,
 			emailFrom,
 			emailTo,
 			fail_silently=False)

	context = {
			'page_title': page_title,
			'form': form,
			'confirm_message': confirm_message,
			}
	template = 'contact/contact.html' 
 	return render(request, template, context)










