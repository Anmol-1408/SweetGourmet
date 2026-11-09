from django.contrib import admin
from accounts.models import UserAccount
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'name', 'is_active', 'is_staff')  # Removed 'is_admin' field
    list_filter = ('is_staff',)  # Filter by 'is_staff' for user management
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),  # Use 'is_superuser' for admin check
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()

admin.site.register(UserAccount, UserModelAdmin)