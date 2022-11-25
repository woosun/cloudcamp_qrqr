from django.contrib import admin
from .models import *

@admin.register(guduck)
class GuduckAdmin(admin.ModelAdmin):
    list_display = ['id','uid', 'pid', 'read_yn', 'create_date']
    list_display_links = ['id']
    list_per_page = 3
    list_filter = ['uid', 'pid','read_yn']