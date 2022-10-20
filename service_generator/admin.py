from django.contrib import admin

from .models import PrayerPosition, ServiceType

# Register your models here.

class PrayerPositionInline(admin.TabularInline):
    model = PrayerPosition
    extra = 1

class ServiceTypeAdmin(admin.ModelAdmin):
    inlines = (PrayerPositionInline,)

admin.site.register(ServiceType, ServiceTypeAdmin)