from django.contrib import admin
from .models import Product, Category, Color, Brand, Picture

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)