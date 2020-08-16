from django.contrib import admin
from .models import User, listings, bid, comments, watch_list
# Register your models here.

admin.site.register(User)
admin.site.register(listings)
admin.site.register(bid)
admin.site.register(comments)
admin.site.register(watch_list)