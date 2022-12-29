from django.contrib import admin

from .models import ServiceType, ServiceTypeSection, Section, SectionPrayer

# Register your models here.


class ServiceTypeSectionInline(admin.TabularInline):
    model = ServiceTypeSection
    extra = 1


class ServiceTypeAdmin(admin.ModelAdmin):
    inlines = (ServiceTypeSectionInline,)


admin.site.register(ServiceType, ServiceTypeAdmin)


class SectionPrayerInline(admin.TabularInline):
    model = SectionPrayer
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    inlines = (SectionPrayerInline,)


admin.site.register(Section, SectionAdmin)