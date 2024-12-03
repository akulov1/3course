from django.contrib import admin
from .models import Planet, Satellite, Mission

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'distance_from_sun')
    search_fields = ('name',)
    list_filter = ('type',)

@admin.register(Satellite)
class SatelliteAdmin(admin.ModelAdmin):
    list_display = ('name', 'planet')
    search_fields = ('name',)
    list_filter = ('planet',)

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'planet', 'date')
    search_fields = ('name',)
    list_filter = ('date', 'planet')
