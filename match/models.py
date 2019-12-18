from django.db import models
from django.db.models import Sum
from common.models import State, Address
from users.models import Player


class Team(models.Model):
    name = models.CharField(max_length=254)
    logo = models.ImageField(upload_to='team/')
    club_state = models.ForeignKey(
        State, null=True, blank=True, on_delete=models.SET_NULL)
    player = models.ManyToManyField(
        Player, db_table='TeamPlayer', related_name='teamplayer')

    def __str__(self):
        return self.name

    @property
    def total_point(self):
        return TeamMatchPoint.objects.filter(team__id=self.id).aggregate(Sum('point')).get('point__sum')


class TeamPlayer(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team')
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='player')
    is_active = models.BooleanField(default=True)

    # class Meta:
    #     auto_created = True

    def __str__(self):
        return self.team.name + ' ' + self.player.email


class Match(models.Model):
    TYPE = (
        ('cricket', 'Cricket'),
    )

    title = models.CharField(max_length=254, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(
        Address, null=True, blank=True, on_delete=models.SET_NULL)
    match_type = models.CharField(
        max_length=254, choices=TYPE, default='cricket')
    teams = models.ManyToManyField(
        Team, db_table='TeamMatch', related_name='teams')
    winner_team = models.ForeignKey(
        Team, blank=True, null=True, related_name='winner_team', on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
        return self.team1.name + ' ' + self.team2.name


class TeamMatchPoint(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.team.name + '->' + str(self.point)