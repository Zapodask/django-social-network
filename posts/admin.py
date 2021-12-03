from django.contrib import admin
from posts.models import Post


class Posts(admin.ModelAdmin):
    list_display = ("id", "title", "content", "author", "created_at")
    list_display_links = ("id", "author")
    search_fields = ("id", "author")


admin.site.register(Post, Posts)
