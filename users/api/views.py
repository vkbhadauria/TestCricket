from rest_framework import generics
from match.models import Player
from users.api.serializers import PlayerSerializer


class PlayerViewSet(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
