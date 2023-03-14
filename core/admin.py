from django.contrib import admin
from core.models import Event

class EventAdm(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'create_date')
    list_filter = ('user', 'event_date')

admin.site.register(Event, EventAdm)
