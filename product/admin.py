from django.contrib import admin
from .models import Product, Category, Color, Brand, Picture, Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'score', 'product', 'status',)
    search_fields = ('body', 'user', 'product',)

admin.site.register(Comment, CommentAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'brand', 'category_to_str', 'all_colors_to_str', 'price', 'offer', 'count_sold',)
    fieldsets = (
        ('Product Specifications', {
            'fields': ('name', 'category', 'code', 'brand', 'weight', 'product_models',)
        }),
        ('Default Type', {
            'fields': ('color', 'price',)
        }),
        ('Sales', {
            'fields': ('count_sold',)
        }),
    )
    def category_to_str(self, obj):
        return [category for category in obj.category.all()]
    
    def all_colors_to_str(self,obj):
        return [color for color in obj.color.all()]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)