from django.contrib import admin
from .models import listings, bid, comments
# Register your models here.

admin.site.register(listings)
admin.site.register(bid)
admin.site.register(comments)