from django.contrib import admin
from .models import *

admin.site.register(Cards)
admin.site.register(Clients)
admin.site.register(Purchases)
admin.site.register(Catalogs)
admin.site.register(Products)
admin.site.register(Products_catalogs)
admin.site.register(Special_offers)
admin.site.register(Products_purchases)
admin.site.register(Orders)