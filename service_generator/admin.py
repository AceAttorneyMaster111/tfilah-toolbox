from django.contrib import admin

from .models import Prayer_Position, ServiceType

# Register your models here.

class PrayerPositionInline(admin.TabularInline):
    model = Prayer_Position
    extra = 1

class ServiceTypeAdmin(admin.ModelAdmin):
    inlines = (PrayerPositionInline,)

admin.site.register(ServiceType, ServiceTypeAdmin)