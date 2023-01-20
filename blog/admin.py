from django.contrib import admin
from .models import BlogModel


# Register your models here.

class BlogModelAdmin(admin.ModelAdmin):
    model = BlogModel
    fields = ['title', 'product', 'content','link' ]
    list_display = ['title', 'product', 'content','created','link',]


admin.site.register(BlogModel, BlogModelAdmin)
# admin.site.register(BlogModelAdmin)
