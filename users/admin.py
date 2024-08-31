
from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "login",
        "phone",
    )
    list_filter = ("created_at",)
    search_fields = ("login",)

