from django import template

register = template.Library()




@register.inclusion_tag("tags/login_tag.html")
def logintag(request, request_path):
	return {'request_path': request_path,  
			'request': request }




			