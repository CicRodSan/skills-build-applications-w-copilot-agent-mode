from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

admin.site.register(User)
admin.site.register(Team)

# Register additional models
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)