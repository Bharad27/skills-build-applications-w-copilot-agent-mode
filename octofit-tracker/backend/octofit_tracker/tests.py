from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        user1 = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=user1, type='Running', duration=30, date='2025-10-17')
        Workout.objects.create(name='Super Strength', description='Strength workout')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Team.objects.count(), 2)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
