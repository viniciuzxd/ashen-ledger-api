from rest_framework import serializers
from .models import Build

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ['id', 'user', 'game', 'name', 'main_stat', 'weapon_type', 'created_at']