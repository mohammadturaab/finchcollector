from django.db import models
from django.contrib.auth.models import User

# Create your models here.
POSITIONS = (
    ('Point Guard', 'point guard'),
    ('Shooting Guard', 'shooting guard'),
    ('Small Forward', 'small forward'),
    ('Power Forward', 'power forward'),
    ('Center', 'center')
)
TIMELINE = (
    ('Current', 'current'),
    ('Past', 'Past')
)
class Player(models.Model):
    img = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=POSITIONS)
    time_line = models.CharField(max_length=50, choices=TIMELINE)

    def __str__(self):
        return self.name

class NBA(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    season_wins = models.IntegerField()
    season_losses = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    players = models.ManyToManyField(Player, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']