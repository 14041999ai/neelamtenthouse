from django.contrib import admin

# Register your models here.
from .models import Event, faq

admin.site.register(Event)
admin.site.register(faq)