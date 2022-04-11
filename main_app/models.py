from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NBA(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    season_wins = models.IntegerField()
    season_losses = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']