from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
import search


# Create your views here.


def results(request):
	#get the current search words
	q = request.GET.get('q', '')
	#get current page number, set to 1 if missing
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		page = 1
	#retrieve the matching products
	matching = search.products(q).get('products')
	#generate the paginator object
	paginator = Paginator(matching, settings.PRODUCTS_PER_PAGE)
	try:
		results = paginator.page(page).object_list
	except(InvalidPage, EmptyPage):
		results = paginator.page(1).object_list
	#store the search
	search.store(request, q)
	page_title = 'Search Results for:' + q
	template = 'search/results.html'
	context = {
			  'page_title': page_title,
			  'q': q,
			  'page': page,
			  'paginator': paginator,
			  'results': results,
			  }
	return render(request, template, context) 


	







