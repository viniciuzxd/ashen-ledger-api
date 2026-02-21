# ⚔️ Ashen Ledger API

**Ashen Ledger** é um sistema de rastreamento e análise de performance para jogos do gênero Souls-like (Elden Ring, Dark Souls, Lies of P, etc). A API não apenas armazena suas vitórias, mas utiliza cálculos estatísticos para determinar o índice de dificuldade real de cada chefe.



[Image of normal distribution curve with Z-score areas]


## 🧠 A Inteligência (Z-Score Analytics)
O diferencial deste projeto é o uso do **Z-Score (Escore Padrão)** para classificar a dificuldade dos bosses. 

A fórmula aplicada é:
$$Z = \frac{x - \mu}{\sigma}$$

Onde a API calcula a média de tentativas do jogador ($\mu$) e o desvio padrão ($\sigma$) de todo o jogo para identificar quais chefes estão acima ou abaixo da curva de dificuldade esperada.

## 🚀 Tecnologias
* **Python 3.14**
* **Django & Django Rest Framework** (API Robustez)
* **SQLite** (Desenvolvimento)
* **Matemática Estatística** (Motor Analítico)

## 🛠️ Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/ashen-ledger-api.git](https://github.com/SEU_USUARIO/ashen-ledger-api.git)

**Crie e ative o ambiente virtual:**

    python -m venv venv
    # No Windows:
    venv\Scripts\activate

**Instale as dependências:**

    Bash
    pip install django djangorestframework django-filter

**Rode as migrações e ligue o servidor:**

    python manage.py migrate
    python manage.py runserver

## 🛣️ Endpoints Principais
GET /api/games/: Lista de jogos suportados.

GET /api/bosses/: Lista de chefes e seus respectivos Z-Scores de dificuldade.

POST /api/games/{id}/calculate_difficulty/: Aciona o motor analítico para o jogo específico.

Desenvolvido por Marcos Vinícius N. Silva como um projeto de análise de dados aplicada a games.