from django.views.generic.base import View
from django.shortcuts import render


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class TeamDetail(View):
    def get(self, request, *args, **kwargs):
        return render(request, "team_details.html")
