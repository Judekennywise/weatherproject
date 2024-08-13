from django.db import models

# Create your models here.
class Names(models.Model):
    names = models.CharField(max_length = 100)

    def __str__(self):
        return self.names
    
from django.contrib.auth.models import User

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city_name} ({self.user.username})"
