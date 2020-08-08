from django.contrib import admin
from .models import listings, bid, comments, watch_list
# Register your models here.

admin.site.register(listings)
admin.site.register(bid)
admin.site.register(comments)
admin.site.register(watch_list)