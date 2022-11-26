from django.contrib import admin
from .models import *
from django.db.models import Q

class GuduckAdmin(admin.ModelAdmin):
#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == "pid":
#            print(db_field)
#            print(request)
#            kwargs["queryset"] = Product.objects.filter(owner=request.uid)
#        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    models = guduck
    list_display = ['id','uid', 'get_pid_name', 'read_yn', 'create_date']
    list_display_links = ['id']
    list_per_page = 3
    list_filter = ['uid','read_yn']

    fieldsets = (
        (None,{"fields": ('uid','pid','read_yn',)},),
    )
    def get_pid_name(self, obj):
        return obj.pid.name

#https://wonpaper.tistory.com/476
admin.site.register(guduck, GuduckAdmin)