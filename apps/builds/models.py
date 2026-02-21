from django.db import models
from apps.users.models import User
from apps.games.models import Game

class Build(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='builds')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='builds')
    name = models.CharField(max_length=100)
    main_stat = models.CharField(max_length=50)  # Ex: STR, DEX, INT
    weapon_type = models.CharField(max_length=100) # Ex: Colossal Sword, Katana
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"