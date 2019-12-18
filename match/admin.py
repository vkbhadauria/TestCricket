from django.contrib import admin
from match.models import Team, Match, TeamPlayer, TeamMatch, TeamMatchPoint

admin.site.register(Team)
admin.site.register(Match)
admin.site.register(TeamPlayer)
admin.site.register(TeamMatch)
admin.site.register(TeamMatchPoint)
