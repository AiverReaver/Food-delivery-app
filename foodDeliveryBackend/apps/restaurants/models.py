from django.db import models
from apps.users.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
