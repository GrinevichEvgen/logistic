from django.contrib import admin

from routes.models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    route = ('start_time', 'start_location', 'end_location', 'driver')
