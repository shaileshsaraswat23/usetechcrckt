from django.conf.urls import url
from team.views import teamlist,playerslist,add_team
app_name="team"

urlpatterns = [
    url(r'^$', teamlist, name='teamlist'),
    url(r'^add_team$', add_team,name='add_team'),
    url(r'^playerslist/(?P<id>[0-9]+)/$', playerslist,name='playerslist'),
]
