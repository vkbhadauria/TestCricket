from rest_framework import serializers
from users.models import PlayerProfile, Player


class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = ('image',)


class PlayerSerializer(serializers.ModelSerializer):
    profile = PlayerProfileSerializer()

    class Meta:
        model = Player
        fields = ('email', 'first_name', 'last_name', 'profile')
