from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "create_datetime", "updata_datetime")
    list_display_links = ("id", "title")

admin.site.register(Blog, BlogAdmin)

# Register your models here.
