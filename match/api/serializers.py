from rest_framework import serializers
from match.models import Team, TeamMatchPoint
from users.api.serializers import PlayerSerializer


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'id', 'logo')


class TeamDetailSerializer(TeamListSerializer):
    player = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = TeamListSerializer.Meta.fields + ('total_point', 'player')
