from django.contrib import admin

from .models import AcceptanceAggregate, Image

admin.site.register(AcceptanceAggregate)
admin.site.register(Image)
