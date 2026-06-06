from django.contrib import admin
from .models import GuestbookEntry


@admin.register(GuestbookEntry)
class GuestbookEntryAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_email', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('author_name', 'author_email', 'content')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Информация об авторе', {
            'fields': ('author_name', 'author_email')
        }),
        ('Содержание', {
            'fields': ('content', 'status')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
