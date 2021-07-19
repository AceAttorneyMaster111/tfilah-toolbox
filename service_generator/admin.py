from django.contrib import admin

from .models import *

admin.site.register([Prayer, Chordsheet_Contributor, Artist])

class Prayer_Position_Inline(admin.TabularInline):
    model = Prayer_Position
    extra = 1

class Service_Type_Admin(admin.ModelAdmin):
    inlines = (Prayer_Position_Inline,)

admin.site.register(Service_Type, Service_Type_Admin)

class Chordsheet_Inline(admin.StackedInline):
    model = Chordsheet

class Song_Admin(admin.ModelAdmin):
    inlines = (Chordsheet_Inline,)

admin.site.register(Song, Song_Admin)