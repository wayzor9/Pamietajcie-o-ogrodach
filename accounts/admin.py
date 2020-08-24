from django.contrib import admin

from accounts.models import User, UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_active", "is_superuser")
    list_filter = ("is_active",)
    ordering = ("is_superuser",)


admin.site.register(UserProfile)
