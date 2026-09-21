from django.contrib import admin
from .models import *

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'Category', 'image', 'date_added')


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)