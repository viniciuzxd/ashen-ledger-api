from django.db import models
from apps.games.models import Game

class Boss(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='bosses')
    name = models.CharField(max_length=150)
    is_optional = models.BooleanField(default=False)
    difficulty_rating = models.FloatField(default=0.0) # Atualizado via job batch depois

    def __str__(self):
        return f"{self.name} ({self.game.name})"