from django.apps import AppConfig

class SessionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sessions'
    label = 'play_sessions'  # <-- Adicione esta linha! O Django usará este apelido.