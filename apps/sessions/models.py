from django.db import models
from apps.users.models import User
from apps.bosses.models import Boss
from apps.builds.models import Build

class PlaySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE, related_name='sessions')
    build = models.ForeignKey(Build, on_delete=models.SET_NULL, null=True, blank=True)
    
    attempts = models.PositiveIntegerField(help_text="Número de tentativas nesta sessão")
    duration_minutes = models.PositiveIntegerField(help_text="Duração em minutos")
    is_victory = models.BooleanField(default=False, help_text="Derrotou o boss nesta sessão?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Vitória" if self.is_victory else "Derrota/Desistência"
        return f"{self.user.username} vs {self.boss.name} - {self.attempts} tries ({status})"