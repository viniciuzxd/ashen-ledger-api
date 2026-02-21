from django.contrib import admin
from .models import Build

@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'game', 'main_stat', 'weapon_type')