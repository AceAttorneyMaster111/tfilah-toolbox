from django.contrib import admin
from django.http import HttpRequest

from .models import *

admin.site.register([Prayer, Artist])


class ChordsheetInline(admin.StackedInline):
    model = Chordsheet


class SongAdmin(admin.ModelAdmin):
    inlines = (ChordsheetInline,)


admin.site.register(Song, SongAdmin)


class IndexHideAdmin(admin.ModelAdmin):
    def has_module_permission(self, request: HttpRequest):
        return False


admin.site.register([SongTag, PrayerTag, ChordsheetContributor], IndexHideAdmin)
