from django.db import models

class User(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=1200)

class data(models.Model):
    pass
class figure(models.Model):
    pass