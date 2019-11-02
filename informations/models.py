from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Survivor(models.Model):
    role = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    rumor = models.TextField()
    like_users = models.ManyToManyField(get_user_model(), related_name="like_survivors")
    def __str__(self):
        return self.name

class Hunter(models.Model):
    role = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    rumor = models.TextField()
    like_users = models.ManyToManyField(get_user_model(), related_name="like_hunters")
    def __str__(self):
        return self.name
    