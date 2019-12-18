from django.urls import path
from match.api.views import TeamViewSet, TeamDetail
urlpatterns = [
    path('', TeamViewSet.as_view()),
    path('<pk>/', TeamDetail.as_view()),
]
