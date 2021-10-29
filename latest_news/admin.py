from django.contrib import admin

from .models import News, Category


class NewsAdmin (admin.ModelAdmin):
    list_display = ('number', 'title', 'slug', 'category', 'created_at', 'file', 'is_published',)
    list_display_links = ('number', 'title',)
    search_fields = ('number', 'title', 'content', 'created_at',)
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published',)


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'cat_title',)
    list_display_links = ('id', 'cat_title',)
    search_fields = ('cat_title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
