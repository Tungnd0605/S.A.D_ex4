from django.contrib import admin
from .models import Manager
# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "address")

admin.site.register(Manager, ManagerAdmin)