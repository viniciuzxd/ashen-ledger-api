from rest_framework import serializers
from .models import PlaySession
from apps.bosses.serializers import BossSerializer # <-- Adicione 'apps.' aqui!

class PlaySessionSerializer(serializers.ModelSerializer):
    boss_details = BossSerializer(source='boss', read_only=True)

    class Meta:
        model = PlaySession
        fields = ['id', 'user', 'boss', 'boss_details', 'build', 'attempts', 'duration_minutes', 'is_victory', 'created_at']