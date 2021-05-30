from django.contrib import admin
from .models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display=('name','auther','title','publish_date')
    list_filter = ('auther','publish_date')
    search_fields = ('name','title')
#admin.site.register(Books)