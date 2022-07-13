from django.contrib import admin

from .models import *

admin.site.register([Prayer, Chordsheet_Contributor, Artist])

class Chordsheet_Inline(admin.StackedInline):
    model = Chordsheet

class Song_Admin(admin.ModelAdmin):
    inlines = (Chordsheet_Inline,)

admin.site.register(Song, Song_Admin)

class Tag_Admin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

admin.site.register([Song_Tag, Prayer_Tag], Tag_Admin)