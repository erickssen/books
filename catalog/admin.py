from django.contrib import admin
from .models import Product, Category, ProductReview
from .forms import ProductAdminForm
 




# Register your models here.

class ProductAdmin(admin.ModelAdmin):

	form = ProductAdminForm  
	# sets values for how the admin site lists products
	list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at')
	list_display_links = ('name',)
	list_per_page = 50
	ordering = ['-created_at']
	search_fields = ['name', 'description', 'meta_keywords', ]
	exclude = ('created_at', 'updated_at')

	# sets up slug to be generated from product name
	prepopulated_fields = { 'slug': ('name', ) }

	# register Product model with admin site
admin.site.register(Product, ProductAdmin) 





class CategoryAdmin(admin.ModelAdmin):

	#sets up values for how admin site lists categories
	list_display = ('name', 'created_at', 'updated_at', )
	list_display_links = ('name',)
	list_per_page = 20
	ordering = ['name']
	search_fields = ['name', 'description', 'meta_keywords', ]
	exclude = ('created_at', 'updated_at', )

	#sets up slug to be created from category name
	prepopulated_fields = {'slug': ('name', ) }

admin.site.register(Category, CategoryAdmin)

	



class ProductReviewAdmin(admin.ModelAdmin):
	list_display = ('product', 'user', 'title', 'date', 'rating', 'is_approved') 
	list_per_page = 20
	list_filter = ('product', 'user', 'is_approved')
	ordering = ['date']
	search_fields = ['user','content','title']

admin.site.register(ProductReview, ProductReviewAdmin) 












