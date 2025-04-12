from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Remover registro de modelos incompatíveis com o Django Admin
# O Django Admin não será usado para os modelos baseados em pymongo.