from django.db.models import Avg, StdDev
from apps.bosses.models import Boss
from apps.sessions.models import PlaySession

def calculate_game_zscores(game):
    """
    Calcula o Z-Score de dificuldade para todos os bosses de um jogo específico,
    baseado nas sessões em que o jogador saiu vitorioso.
    """
    # 1. Filtramos apenas as sessões de VITÓRIA desse jogo específico
    valid_sessions = PlaySession.objects.filter(boss__game=game, is_victory=True)
    
    if not valid_sessions.exists():
        return "Nenhuma sessão de vitória encontrada para este jogo."

    # 2. Calculamos a Média Global (mu) e o Desvio Padrão Global (sigma)
    stats = valid_sessions.aggregate(
        mu=Avg('attempts'),
        sigma=StdDev('attempts')
    )
    
    mu = stats['mu']
    sigma = stats['sigma']

    # Proteção contra divisão por zero (se todos mataram de primeira, sigma é 0)
    if not sigma or sigma == 0:
        sigma = 1.0

    # 3. Iteramos sobre cada Boss do jogo para achar o 'x' e aplicar a fórmula
    bosses = Boss.objects.filter(game=game)
    updated_count = 0
    
    for boss in bosses:
        boss_sessions = valid_sessions.filter(boss=boss)
        
        if boss_sessions.exists():
            # Média de tentativas específicas deste Boss (x)
            x = boss_sessions.aggregate(avg_attempts=Avg('attempts'))['avg_attempts']
            
            # 4. A Fórmula Mágica do Z-Score
            z_score = (x - mu) / sigma
            
            # Salvamos no banco de dados com 2 casas decimais
            boss.difficulty_rating = round(z_score, 2)
            boss.save()
            updated_count += 1

    return f"Inteligência rodada! {updated_count} Bosses atualizados com sucesso."