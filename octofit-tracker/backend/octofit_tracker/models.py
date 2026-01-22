from django.db import models
from django.contrib.auth.models import AbstractUser

# User model
class User(AbstractUser):
    # Additional fields can be added here
    pass

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField('User', related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Activity model
class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    distance = models.FloatField(help_text='Distance in kilometers', null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

# Workout model
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    suggested_for = models.ManyToManyField('User', related_name='suggested_workouts', blank=True)

# Leaderboard model (denormalized for fast access)
class Leaderboard(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['rank']
