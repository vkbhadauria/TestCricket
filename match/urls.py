from django.urls import path, include
from match.views import Home, TeamDetail
urlpatterns = [
    path('', Home.as_view()),
    path('team_details/<pk>', TeamDetail.as_view())

]
