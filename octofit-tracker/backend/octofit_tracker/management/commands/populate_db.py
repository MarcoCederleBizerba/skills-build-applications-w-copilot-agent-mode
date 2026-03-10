from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()


        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captainamerica@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities (embedded user)
        Activity.objects.create(
            user={
                'email': users[0].email,
                'name': users[0].name,
                'team': users[0].team,
                'is_superhero': users[0].is_superhero
            },
            type='Running', duration=30, date=timezone.now()
        )
        Activity.objects.create(
            user={
                'email': users[1].email,
                'name': users[1].name,
                'team': users[1].team,
                'is_superhero': users[1].is_superhero
            },
            type='Cycling', duration=45, date=timezone.now()
        )
        Activity.objects.create(
            user={
                'email': users[3].email,
                'name': users[3].name,
                'team': users[3].team,
                'is_superhero': users[3].is_superhero
            },
            type='Swimming', duration=60, date=timezone.now()
        )

        # Leaderboard (embedded team)
        Leaderboard.objects.create(
            team={
                'name': marvel.name,
                'description': marvel.description
            },
            points=150
        )
        Leaderboard.objects.create(
            team={
                'name': dc.name,
                'description': dc.description
            },
            points=120
        )

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for superheroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
