from django.db import models
from django.utils.html import format_html
# Create your models here.
class teamform(models.Model):
    name = models.CharField(max_length=50)
    logouri = models.ImageField(upload_to='team')
    clubstate = models.CharField(max_length=100)

    def team_logo(self):
            return format_html('<img src="/media/%s" width="30",height="30"/>' % self.logouri)
    team_logo.allow_tags = True

    def __str__(self):
        return self.name
