
from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "header",
        "author",
    )
    list_filter = ("header",)
    search_fields = ("header",)
