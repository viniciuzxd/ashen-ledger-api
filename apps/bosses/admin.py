from django.contrib import admin
from .models import Boss

@admin.register(Boss)
class BossAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'is_optional', 'difficulty_rating')
    list_filter = ('game', 'is_optional') # Adiciona filtros laterais