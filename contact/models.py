from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=10)
    enroll = models.CharField(max_length=11)
    group = models.CharField(max_length=5)
    year = models.CharField(max_length=8)
    def __str__(self):
        return self.name
