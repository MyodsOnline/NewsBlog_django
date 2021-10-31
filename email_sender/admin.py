from django.contrib import admin

from .models import Email


class EmailAdmin (admin.ModelAdmin):
    list_display = ('number', 'date', 'time', 'text', 'file', 'author', 'is_ok',)
    list_display_links = ('number',)
    search_fields = ('number', 'text', 'author',)
    list_editable = ('is_ok',)
    list_filter = ('number', 'is_ok',)


admin.site.register(Email, EmailAdmin)
