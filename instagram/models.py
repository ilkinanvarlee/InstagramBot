from django.db import models
from django.contrib.auth.models import User


class Instagram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instagram', null=True, blank=True)
    instagram_username = models.CharField(max_length=30)
    instagram_password = models.CharField(max_length=30)
    followers = models.IntegerField(null=True, blank=True)
    following = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    # objects = models.Manager()
