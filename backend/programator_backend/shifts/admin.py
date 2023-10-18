from django.contrib import admin

from .models import Shift, Event, Worker


admin.site.register(Shift)
admin.site.register(Event)
admin.site.register(Worker)
