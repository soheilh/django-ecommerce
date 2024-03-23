from django.contrib import admin
from .models import Post, Category, Comment

# Register Post Model
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'status', 'category_to_str',)
	list_filter = ('publish', 'status',)
	search_fields = ('title', 'description', 'content',)
	prepopulated_fields = {'slug': ('title',)}
	ordering = ('-status', '-publish',)
	# exclude = ('author', )

	def category_to_str(self, obj):
		return [category for category in obj.category.all()]
	category_to_str.short_description = 'Categories'

admin.site.register(Post, PostAdmin)

# Register Category Model
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'status',)
	list_filter = ('status',)
	search_fields = ('name', )
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)