from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import *

class UserAdmin(BaseUserAdmin):
    """Custom User Admin"""
    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        ('Main', {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('Important Dates',{'fields': ('last_login',)})
    )

    readonly_fields = ['last_login']
    add_fieldsets= (
        (None,{
            'classes': ('wide',),
            'fields':
            ('email', 'password1', 'password2','name','is_active','is_staff','is_superuser',),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Ingredient)