
from rest_framework import viewsets, permissions, response, decorators
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	permission_classes = [permissions.AllowAny]

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer
	permission_classes = [permissions.AllowAny]

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer
	permission_classes = [permissions.AllowAny]

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer
	permission_classes = [permissions.AllowAny]

@decorators.api_view(['GET'])
def api_root(request, format=None):

	import os
	codespace_name = os.environ.get('CODESPACE_NAME')
	if codespace_name:
		base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
		def url(path):
			return f"{base_url}{path}/"
	else:
		def url(path):
			return request.build_absolute_uri(f"/api/{path}/")
	return response.Response({
		'users': url('users'),
		'teams': url('teams'),
		'activities': url('activities'),
		'leaderboard': url('leaderboard'),
		'workouts': url('workouts'),
	})
