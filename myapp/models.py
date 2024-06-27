from django.db import models
from datetime import date

# Create your models here.
class Post (models.Model):
    header=models.CharField(max_length=300)
    body=models.CharField(max_length=10000)
    date_post=models.DateField(default=date.today())
