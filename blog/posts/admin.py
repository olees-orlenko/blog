from django.contrib import admin

from .models import Blog, Follow, News, Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["user"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "pub_date"]
    list_filter = ["author"]
    search_fields = ["title", "text"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "is_read"]
    list_filter = ["user", "is_read"]


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ["follower", "following"]
    list_filter = ["follower", "following"]
