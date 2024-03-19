from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock', 'sold')

admin.site.register(Book, BookAdmin)