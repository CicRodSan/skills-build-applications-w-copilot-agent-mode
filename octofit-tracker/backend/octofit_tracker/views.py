from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from django.conf import settings

# Configurar conexão com o MongoDB
client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
db = client[settings.DATABASES['default']['NAME']]

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'http://localhost:8000/api/users/',
        'teams': 'http://localhost:8000/api/teams/',
        'activities': 'http://localhost:8000/api/activities/',
        'leaderboard': 'http://localhost:8000/api/leaderboard/',
        'workouts': 'http://localhost:8000/api/workouts/'
    })

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = list(db.users.find())
        return Response(users)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = list(db.teams.find())
        return Response(teams)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = list(db.activity.find())
        return Response(activities)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboard = list(db.leaderboard.find())
        return Response(leaderboard)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = list(db.workouts.find())
        return Response(workouts)