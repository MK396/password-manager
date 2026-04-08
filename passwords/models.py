from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.website} - {self.username}"