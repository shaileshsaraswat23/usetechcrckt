from django.shortcuts import render
from team.models import teamform
from .forms import addteam
from player.models import players
from match.models import matches,match_details
from django.contrib import messages
from team.helpers import player_history


# Create your views here.
def teamlist(request):
    teams = teamform.objects.all()
    context={'data':teams}
    return render(request, "team/team_list.html",context)

def add_team(request):
    team_form = addteam()
    if request.method == "POST":
        team_form = addteam(request.POST,request.FILES)
        if team_form.is_valid():
            try:
                team_instance = team_form.save(commit=False)
                team_instance.save()
                messages.info(request, "New team %s Added." % team_instance.name)
                return redirect("team:teamlist")
            except Exception as e:
                context = { 'form': team_form }
                return render(request,"team/add_team.html",context)
        else:
            context={'form':team_form}
            return render(request,"team/add_team.html",context)
    else:
        context={'form':team_form}
        return render(request,"team/add_team.html",context)



def playerslist(request,id):
    teamid=id
    # print('teamid',teamid)
    player=players.objects.filter(teamid_id=teamid)
    playersss=player_history(teamid)
    allmatches = matches.objects.filter()

    team=teamform.objects.get(id=teamid)
    print(playersss)
    context={'data':playersss,'teamname':team,'match':allmatches}
    return render(request, "team/playerslist.html",context)
