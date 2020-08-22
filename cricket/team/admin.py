from django.contrib import admin
from django.contrib.auth.models import Group
from team.models import teamform

# Register your models here.
class teaminfo(admin.ModelAdmin):
    list_display = ['name','team_logo']
    list_filter=('name',)
admin.site.site_header = 'Cricket'
admin.site.register(teamform,teaminfo)
admin.site.unregister(Group)
