from pymongo import MongoClient

def initialize_mongo_db():
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']

    # Criar coleções e índices
    db.create_collection('users')
    db.create_collection('teams')
    db.create_collection('activities')
    db.create_collection('leaderboard')
    db.create_collection('workouts')

    db.users.create_index('email', unique=True)
    db.teams.create_index('name', unique=True)
    db.activities.create_index('activity_id', unique=True)
    db.leaderboard.create_index('leaderboard_id', unique=True)
    db.workouts.create_index('workout_id', unique=True)

    print("Banco de dados MongoDB inicializado com sucesso!")

if __name__ == "__main__":
    initialize_mongo_db()