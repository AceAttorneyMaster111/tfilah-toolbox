from django.contrib import admin

from .models import *

admin.site.register([Prayer, Artist])

class Chordsheet_Inline(admin.StackedInline):
    model = Chordsheet

class Song_Admin(admin.ModelAdmin):
    inlines = (Chordsheet_Inline,)

admin.site.register(Song, Song_Admin)

class Index_Hide_Admin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

admin.site.register([Song_Tag, Prayer_Tag, Chordsheet_Contributor], Index_Hide_Admin)