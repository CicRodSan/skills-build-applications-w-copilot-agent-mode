import json
from pymongo import MongoClient
from django.core.management.base import BaseCommand
from pathlib import Path

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Load test data from JSON file
        base_dir = Path(__file__).resolve().parent.parent.parent
        test_data_path = base_dir / 'test_data.json'
        with open(test_data_path, 'r') as file:
            test_data = json.load(file)

        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Insert data into collections
        db.users.insert_many(test_data['users'])
        db.teams.insert_many(test_data['teams'])
        db.activities.insert_many(test_data['activities'])
        db.leaderboard.insert_many(test_data['leaderboard'])
        db.workouts.insert_many(test_data['workouts'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
