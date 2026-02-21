from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Registra o seu usuário customizado usando a interface padrão do Django
admin.site.register(User, UserAdmin)