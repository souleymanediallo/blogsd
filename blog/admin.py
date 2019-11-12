from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'update',)
    list_display_links = ('title',)
    search_fields = ['title']

