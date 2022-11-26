from django.contrib import admin
from .models import *

@admin.register(push)
class PushAdmin(admin.ModelAdmin):
    list_display = ['id', 'gid', 'try_yn','reg_date']
    list_display_links = ['id']
    list_per_page = 3
    list_filter = ['gid','try_yn']
