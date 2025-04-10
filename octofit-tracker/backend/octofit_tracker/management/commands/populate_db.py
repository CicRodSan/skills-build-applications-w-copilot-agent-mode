from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Popula o banco de dados MongoDB com dados de exemplo'

    def handle(self, *args, **kwargs):
        # Criar usuários
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Criar times
        team1 = Team.objects.create(name='Team Alpha', members=[user1, user2])

        # Criar atividades
        Activity.objects.create(user=user1, activity_type='Running', duration='00:30:00')
        Activity.objects.create(user=user2, activity_type='Cycling', duration='01:00:00')

        # Criar leaderboard
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Criar treinos
        Workout.objects.create(name='Morning Run', description='A quick morning run to start the day.')
        Workout.objects.create(name='Evening Yoga', description='Relaxing yoga session in the evening.')

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
