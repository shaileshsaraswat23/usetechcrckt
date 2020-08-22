from django.contrib.auth.models import User
from team.models import teamform
from match.models import matches,match_details
from player.models import players
from django.db.models import Avg, Max, Min, Sum, Count


## used to give player history like: Max run,Ma wicket,Total Run,Total match
def player_history(teamid):
    playersinfo = players.objects.filter(teamid_id=teamid)
    playersrecord = []
    for plsi in playersinfo:
        tech_sec = match_details.objects.filter(playerid=plsi.id).aggregate(Max('run'))
        wicket_m = match_details.objects.filter(playerid=plsi.id).aggregate(Max('wicket'))
        totalmatch=match_details.objects.filter(playerid=plsi.id).count()
        totalrun = match_details.objects.filter(playerid=plsi.id).aggregate(Sum('run'))

        playersrecord.append({'totalrun':totalrun['run__sum'],'totalmatch':totalmatch,'run':tech_sec['run__max'],'wicket':wicket_m['wicket__max'],'fname':plsi.firstName,
        'lname':plsi.lastName,'image':plsi.imageUri,'playernum':plsi.playernum
        })
    return playersrecord
