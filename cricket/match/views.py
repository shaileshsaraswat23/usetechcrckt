from django.shortcuts import render
from match.models import matches,match_details

# Create your views here.
# def matchfixtures(request):
#     allmatches = matches.objects.all()
#     context={'data':allmatches}
#     return render(request, "team/team_list.html",context)

def matchdetails(request,id):
    matchid=id
    # print('teamid',teamid)
    # player=players.objects.filter(teamid_id=matchid)
    # allmatches = matches.objects.get(matchid=matchid)
    matchdetail=match_details.objects.filter(matchid=matchid)
    # print(matchdetail)
    # team=teamform.objects.get(id=teamid)
    # print(team)
    context={'data':matchdetail}
    return render(request, "team/match_details.html",context)
