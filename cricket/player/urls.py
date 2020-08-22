from django.conf.urls import url
from player.views import playerlist,newplayer
app_name="player"

urlpatterns = [
    url(r'^playerlist$', playerlist, name='playerlist'),
    url(r'^newplayer$', newplayer,name='newplayer'),
]
