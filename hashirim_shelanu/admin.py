from django.contrib import admin

from .models import *

admin.site.register([Prayer, Artist])

class ChordsheetInline(admin.StackedInline):
    model = Chordsheet

class SongAdmin(admin.ModelAdmin):
    inlines = (ChordsheetInline,)

admin.site.register(Song, SongAdmin)

class IndexHideAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

admin.site.register([SongTag, Prayer_Tag, ChordsheetContributor], IndexHideAdmin)