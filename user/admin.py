from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminUser, CustomerUser, AuthorUser

# Register AdminUser model
class AdminUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'name', 'lastname')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('is_staff',)

admin.site.register(AdminUser, AdminUserAdmin)

# Register CustoemrUser model
class CustomerUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'name', 'lastname')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        ('Account Information', {
            'fields': ('phone', 'password', )
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', )
        }),
        ('Residence and bank information', {
            'fields': ('home_state', 'home_city', 'home_address', 'home_postal_code', 'shaba', )
        }),
        ('Favorites', {
            'fields': ('favorite',)
        }),
    )
    add_fieldsets = (
        ('Account Information', {
            'fields': ('phone', 'password1', 'password2',)
        }),
    )
    readonly_fields = ('favorite', )
    
    def save_model(self, request, obj, form, change):
        obj.username = obj.phone
        super(CustomerUserAdmin, self).save_model(request, obj, form, change)

admin.site.register(CustomerUser, CustomerUserAdmin)


# Register AuthorUser model
class AuthorUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'name', 'lastname', "bio", "telegram", "instagram", "twitter", "facebook")
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        ('Account Information', {
            'fields': ('username', 'password', )
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'bio', 'telegram', 'instagram', 'twitter', 'facebook')
        }),
    )
    add_fieldsets = (
        ('Account Information', {
            'fields': ('username', 'password1', 'password2',)
        }),
    )
    readonly_fields = ('is_staff',)

admin.site.register(AuthorUser, AuthorUserAdmin)
