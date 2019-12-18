from django.contrib import admin
from users.models import Player, PlayerProfile
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(Player)
admin.site.unregister(Group)
admin.site.register(PlayerProfile)