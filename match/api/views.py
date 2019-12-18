from django.shortcuts import render
from rest_framework import generics
from match.models import Team
from .serializers import TeamListSerializer, TeamDetailSerializer 


class TeamViewSet(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer


class TeamDetail(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer