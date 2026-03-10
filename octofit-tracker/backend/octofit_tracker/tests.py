from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", team="Test Team", is_superhero=True)
        self.assertEqual(user.name, "Test User")
        self.assertTrue(user.is_superhero)

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team", description="A test team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = {"name": "Test User", "email": "test@example.com"}
        activity = Activity.objects.create(user=user, type="Running", duration=30, date="2026-03-10")
        self.assertEqual(activity.type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = {"name": "Test Team"}
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do pushups", suggested_for="Test Team")
        self.assertEqual(workout.name, "Pushups")
