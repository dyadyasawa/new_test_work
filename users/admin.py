
from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "login",
        "phone",
    )
    list_filter = ("login",)
    search_fields = ("login",)

