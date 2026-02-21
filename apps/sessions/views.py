from rest_framework import viewsets
from .models import PlaySession
from .serializers import PlaySessionSerializer

class PlaySessionViewSet(viewsets.ModelViewSet):
    queryset = PlaySession.objects.all()
    serializer_class = PlaySessionSerializer