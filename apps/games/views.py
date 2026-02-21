from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer

# Importando a nossa magia matemática!
from apps.bosses.services import calculate_game_zscores

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # Criando a alavanca na API (/api/games/{id}/calculate_difficulty/)
    @action(detail=True, methods=['post'])
    def calculate_difficulty(self, request, pk=None):
        # 1. Pega o jogo específico que estamos acessando (Ex: Elden Ring)
        game = self.get_object() 
        
        # 2. Roda o motor do Z-Score
        result_message = calculate_game_zscores(game)
        
        # 3. Devolve a resposta em JSON avisando que deu certo
        return Response({'status': result_message})