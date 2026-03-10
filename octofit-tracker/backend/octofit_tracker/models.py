from djongo import models



# Abstract embedded classes for Djongo
class EmbeddedTeam(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        abstract = True

class EmbeddedUser(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    is_superhero = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Main models
class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    is_superhero = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.JSONField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.user.get('name', '')} - {self.type}"

class Leaderboard(models.Model):
    team = models.JSONField()
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.get('name', '')} - {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)

    def __str__(self):
        return self.name
