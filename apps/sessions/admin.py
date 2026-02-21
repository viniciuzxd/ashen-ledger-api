from django.contrib import admin
from .models import PlaySession

@admin.register(PlaySession)
class PlaySessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'boss', 'attempts', 'is_victory', 'created_at')
    list_filter = ('is_victory',) # Filtro rápido para vitórias/derrotas