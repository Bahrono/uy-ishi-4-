from django.contrib import admin
from .models import Books, Authors
from import_export.admin import ImportExportModelAdmin

@admin.register(Books)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_display_links = ('title',)
    ordering = ('title',)
    search_fields = ('title', 'author__name')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Authors)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('name', 'birthdate')
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
