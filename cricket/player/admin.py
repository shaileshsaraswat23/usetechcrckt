from django.contrib import admin
# from django.contrib.auth.models import Group
from player.models import players

# Register your models here.
class playerinfo(admin.ModelAdmin):
    list_display = ['firstName','player_logo']
    list_filter=('firstName',)
admin.site.site_header = 'Cricket'
admin.site.register(players,playerinfo)
# admin.site.unregister(Group)
