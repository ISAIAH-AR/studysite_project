from django.db import models

# Create your models here.
class SignUpModel(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
