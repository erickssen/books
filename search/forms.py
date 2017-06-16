from django import forms
from .models import SearchTerm





class SearchForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		default_text = ''
		self.fields['q'].widget.attrs['value'] = default_text
		self.fields['q'].widget.attrs['onfocus'] = '' #" if (this.value==' "  + default_text +  " ').this.value = ''  "

	class Meta:
		model = SearchTerm
		fields = ('q', ) 





