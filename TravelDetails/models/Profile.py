from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    gender_choices = [('male','Male'),('female','Female')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=15,choices=gender_choices,default="male")

    def __str__(self):
        return self.user.username