from django.contrib import admin

# Register your models here.
from .models import Blog


class ReadOnlyFieldBlog(admin.ModelAdmin):
    readonly_fields = [
        'published',
        'updated',
        'slug'
    ]


admin.site.register(Blog, ReadOnlyFieldBlog)
