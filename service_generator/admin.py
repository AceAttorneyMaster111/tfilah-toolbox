from django.contrib import admin

from .models import Prayer_Position, Service_Type

# Register your models here.

class Prayer_Position_Inline(admin.TabularInline):
    model = Prayer_Position
    extra = 1

class Service_Type_Admin(admin.ModelAdmin):
    inlines = (Prayer_Position_Inline,)

admin.site.register(Service_Type, Service_Type_Admin)