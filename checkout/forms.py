from django import forms
from .models import Order
import datetime
import re
import logging




def strip_non_numbers(data):
	""" gets rid of all non-number characters """
	non_numbers = re.compile('\D')
	return non_numbers.sub('', data)




class CheckoutForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CheckoutForm, self).__init__(*args, **kwargs)


		# override defaults attributes
		for field in self.fields:
			self.fields[field].widget.attrs['size'] = '50'
		# self.fields['shipping_state'].widget.attrs['size'] = '30'
		# self.fields['shipping_zip'].widget.attrs['size'] = '30'


	class Meta:
		model = Order
		fields = ('shipping_name', 'shipping_address_1', 'shipping_address_2', 'shipping_city', 'shipping_zip', 'shipping_state', 'shipping_country', 'email', 'phone', )
		 																					                                                     																
		 
	   


	def clean_phone(self):
		phone = self.cleaned_data['phone']
		stripped_phone = strip_non_numbers(phone)
		if len(stripped_phone) < 10:
			raise forms.ValidationError('Enter a valid phone number with area code. (e.g. 555-555-5555)')
		return self.cleaned_data['phone']

		



















	