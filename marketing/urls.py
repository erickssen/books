from .sitemap import SITEMAPS
from django.contrib.sitemaps.views import sitemap


patterns = [

	url(r'^sitemap\.xml$', sitemap, {'sitemaps': SITEMAPS}, name='django.contrib.sitemaps.views.sitemap'),

]


