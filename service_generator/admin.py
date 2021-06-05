from django.contrib import admin

from .models import Prayer, Prayer_Position, Service_Type, Song

admin.site.register([Prayer, Song])

class Prayer_Position_Inline(admin.TabularInline):
    model = Prayer_Position
    extra = 1

class Service_Type_Admin(admin.ModelAdmin):
    inlines = (Prayer_Position_Inline,)

admin.site.register(Service_Type, Service_Type_Admin)