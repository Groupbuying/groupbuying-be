from django.db import models

class User(models.Model):
    name = models.CharField(max_length=120)


class NonRegisteredUser(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
