from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'is_published', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'text')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Backend на Python'
admin.site.site_header = 'Управление записями'