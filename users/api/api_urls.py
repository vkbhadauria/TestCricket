from django.urls import path
from users.api.views import PlayerViewSet
urlpatterns = [
    path('', PlayerViewSet.as_view()),
]
