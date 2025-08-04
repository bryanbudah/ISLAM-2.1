from django.contrib import admin

# Register your models here.
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("bio", "profile_picture", "location", "website"),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("bio", "profile_picture", "location", "website"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
