from django import forms
from .models import Product
from .models import ProductReview
import logging
  
 


class ProductAdminForm(forms.ModelForm): 
	
	class Meta:
		model = Product
		exclude = ('created_at', 'updated_at', )

	def clean_price(self):
		if self.cleaned_data['price'] <= 0:
			raise forms.ValidationError('Price must be greater than zero.')
		return self.cleaned_data['price']




class ProductAddToCartForm(forms.Form):
	product_slug = forms.CharField(widget=forms.HiddenInput() )
	quantity = forms.IntegerField(error_messages={'min_value': 1}, initial=1 ) 


	def __init__(self, request=None, *args, **kwargs):
		self.request = request
		super(ProductAddToCartForm, self).__init__(*args, **kwargs)	


	def clean(self):
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError('Cookies must be enabled.')
			return self.cleaned_data


	

class ProductReviewForm(forms.ModelForm):

	class Meta:
		model = ProductReview
		exclude = ('user', 'product', 'is_approved')





















