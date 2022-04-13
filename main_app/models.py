from django.db import models
from django.contrib.auth.models import User

# Create your models here.
POSITIONS = (
    ('pg', 'point guard'),
    ('sg', 'shooting guard'),
    ('sf', 'small forward'),
    ('pf', 'power forward'),
    ('c', 'center')
)
class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=POSITIONS)

    def __str__(self):
        return self.name

class NBA(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    season_wins = models.IntegerField()
    season_losses = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']