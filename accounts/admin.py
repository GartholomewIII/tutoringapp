from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "subjects",
        "days",
        "hours",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("subjects", "days", "hours")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("subjects", "days", "hours")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)