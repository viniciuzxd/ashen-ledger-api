from rest_framework import viewsets
from .models import Boss
from .serializers import BossSerializer

class BossViewSet(viewsets.ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer