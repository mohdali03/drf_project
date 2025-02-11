from django.contrib import admin

from snippets.models import Snippet

# Register your models here.

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','language']
