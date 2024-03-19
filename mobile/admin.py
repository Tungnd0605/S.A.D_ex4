from django.contrib import admin
from .models import Mobile

class MobileAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'stock', 'sold')

admin.site.register(Mobile, MobileAdmin)
