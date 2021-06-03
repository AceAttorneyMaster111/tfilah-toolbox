from django.contrib import admin

from .models import Prayer, Prayer_Position, Service_Type, Song

admin.site.register([Prayer, Prayer_Position, Service_Type, Song])