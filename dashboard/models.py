from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    massage=models.CharField(max_length=500)
