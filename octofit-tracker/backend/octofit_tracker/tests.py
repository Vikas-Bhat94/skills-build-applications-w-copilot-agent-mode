
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
	def test_team_create(self):
		team = Team.objects.create(name='Test Team', description='desc')
		self.assertEqual(str(team), 'Test Team')

	def test_user_create(self):
		team = Team.objects.create(name='Test Team2', description='desc')
		user = User.objects.create(name='Test User', email='test@example.com', team=team)
		self.assertEqual(str(user), 'Test User')

	def test_activity_create(self):
		team = Team.objects.create(name='Test Team3', description='desc')
		user = User.objects.create(name='Test User2', email='test2@example.com', team=team)
		activity = Activity.objects.create(user=user, activity='Run', duration=10)
		self.assertEqual(str(activity), 'Test User2 - Run')

	def test_leaderboard_create(self):
		team = Team.objects.create(name='Test Team4', description='desc')
		leaderboard = Leaderboard.objects.create(team=team, points=42)
		self.assertEqual(str(leaderboard), 'Test Team4: 42')

	def test_workout_create(self):
		workout = Workout.objects.create(name='Workout', suggested_for='Marvel')
		self.assertEqual(str(workout), 'Workout')
