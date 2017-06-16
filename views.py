from django.shortcuts import render
from django.template import RequestContext

def file_not_found_404(request):
	page_title = 'Page Not Found'
	template = '404.html'
	context = {}
	return render(request, template, context)


