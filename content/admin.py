from django.contrib import admin
from .models import City, Image, DaysVisits, Property, Schedule, Visits

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('street', 'value', 'room', 'size', 'city', 'type')
    list_editable = ('value', 'type')
    list_filter = ('city', 'type')

admin.site.register(DaysVisits)
admin.site.register(City)
admin.site.register(Image)
admin.site.register(Schedule)
admin.site.register(Visits)
