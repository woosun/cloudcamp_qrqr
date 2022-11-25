from django.contrib import admin
from .models import *

@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','uid', 'category', 'name', 'display_yn', 'query_yn' ]
    list_display_links = ['id', 'name']
    list_editable = ['category']
    list_per_page = 3
    list_filter = ['category', 'display_yn','query_yn']