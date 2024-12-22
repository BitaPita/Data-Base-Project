from django.db import models
from team.models import teams

class matches(models.Model):
    team1 = models.ForeignKey(teams, on_delete=models.CASCADE,related_name='matches_as_team1' )
    team2 = models.ForeignKey(teams, on_delete=models.CASCADE, null=True, related_name='matches_as_team2')
    opname= models.CharField(null=True,max_length=40)
    isplayed= models.BooleanField(default=False)
    sc1=models.IntegerField(blank=0,null=True)
    sc2 = models.IntegerField(blank=0,null=True)
    date= models.DateTimeField()
    place= models.CharField(max_length=10)


class analysis(models.Model):
    match= models.ForeignKey(matches, on_delete=models.CASCADE,related_name='match')
    desc = models.CharField('Desc', null=True, max_length=1000)
    pic = models.ImageField(upload_to='p1/', null=True, blank=True)
    video = models.FileField(upload_to='v1/', null=True, blank=True)