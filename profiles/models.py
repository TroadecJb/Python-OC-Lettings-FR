from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Class to represent a user's profile

    Attributes
    ----------
    user : int
        Foreign key of the user id, from table auth_user
    favorite_city : str
        name of the favorite city
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
