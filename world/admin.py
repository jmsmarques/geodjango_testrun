from django.contrib.gis import admin

from .models import WorldBorder, GeoPoint

admin.site.register((WorldBorder, GeoPoint), admin.GeoModelAdmin)
