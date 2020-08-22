from django.contrib import admin
# from django.contrib.auth.models import Group
from match.models import matches,match_details

# Register your models here.
class matchinfo(admin.ModelAdmin):
    list_display = ['team_one','team_two','match_winner']
    list_filter=('match_winner',)
admin.site.site_header = 'Cricket'
admin.site.register(matches,matchinfo)
# admin.site.unregister(Group)

# every match details of the players
class matchplayers_details(admin.ModelAdmin):
    list_display = ['playerid','run','wicket']
    list_filter=('playerid',)
admin.site.site_header = 'Cricket'
admin.site.register(match_details,matchplayers_details)
