from rest_framework import serializers
from .models import Boss
from apps.games.serializers import GameSerializer

class BossSerializer(serializers.ModelSerializer):
    # Isso vai trazer os dados do jogo junto com o boss, em vez de só o ID
    game_details = GameSerializer(source='game', read_only=True)

    class Meta:
        model = Boss
        fields = ['id', 'name', 'game', 'game_details', 'is_optional', 'difficulty_rating']