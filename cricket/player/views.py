from django.shortcuts import render
from .models import players
from .forms import addplayer
from django.contrib import messages


# Create your views here.
def playerlist(request):
    allplayers = players.objects.all()
    context={'data':allplayers}
    return render(request, "team/team_list.html",context)

def newplayer(request):
    player_form = addplayer()
    if request.method == "POST":
        player_form = addplayer(request.POST,request.FILES)
        if player_form.is_valid():
            try:
                player_instance = player_form.save(commit=False)
                player_instance.save()
                messages.info(request, "New team %s Added." % player_instance.firstName)
                return redirect("team:teamlist")
            except Exception as e:
                context = { 'form': player_form }
                return render(request,"team/add_player.html",context)
        else:
            context={'form':player_form}
            return render(request,"team/add_player.html",context)
    else:
        context={'form':player_form}
        return render(request,"team/add_player.html",context)
