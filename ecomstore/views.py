from django.shortcuts import render
 


 
def file_not_found_404(request):
	page_title = 'Page Not Found'
	message_404 = 'hello 404'
	template = '404.html'
	context= {
			 'page_title': page_title,
			 'message_404': message_404,
			 }
	 
	return render(request, template, context) 


 

