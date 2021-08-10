from django.contrib import admin

from .models import *

admin.site.register([Prayer, Chordsheet_Contributor, Artist])

class Chordsheet_Inline(admin.StackedInline):
    model = Chordsheet

class Song_Admin(admin.ModelAdmin):
    inlines = (Chordsheet_Inline,)

admin.site.register(Song, Song_Admin)