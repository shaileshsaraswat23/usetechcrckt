from django.db import models
from team.models import teamform
from django.utils.html import format_html

# Create your models here.
class players(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    imageUri = models.ImageField(upload_to='player')
    playernum = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    teamid=models.IntegerField(default=0)
    teamid=models.ForeignKey(teamform,default=0,on_delete=models.PROTECT)

    def player_logo(self):
            return format_html('<img src="/media/%s" width="30",height="30"/>' % self.imageUri)
    player_logo.allow_tags = True

    def __str__(self):
        return self.firstName+' '+self.lastName
