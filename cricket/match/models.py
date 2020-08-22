from django.db import models
from team.models import teamform
from player.models import players

# Create your models here.
class matches(models.Model):
    # team_one=models.IntegerField(default=0)
    # teams = models.ManyToManyField(teamform)
    matchname = models.CharField(max_length=50,default='NULL')
    team_one=models.ForeignKey(teamform,on_delete=models.PROTECT,related_name='home_team')
    team_two=models.ForeignKey(teamform,on_delete=models.PROTECT,related_name='away_team')
    match_winner=models.ForeignKey(teamform,on_delete=models.PROTECT,related_name='winner')

    def __str__(self):
        return str(self.match_winner) if self.match_winner else ''

# players runs on the matches
class match_details(models.Model):
    matchid = models.ForeignKey(matches,on_delete=models.PROTECT,related_name='matchid')
    playerid = models.ForeignKey(players,on_delete=models.PROTECT,related_name='playerid')
    run = models.IntegerField(default=0)
    wicket = models.IntegerField(default=0)

    def __str__(self):
        return str(self.matchid) if self.matchid else ''
