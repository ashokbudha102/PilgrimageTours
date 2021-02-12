from django.db import models

# Create your models here.

class Transaction(models.Model):
    pid=models.CharField(max_length=40)
    rid=models.CharField(max_length=10)
    tamt=models.IntegerField()

    def __str__(self):
        return self.rid

class Serial(models.Model):
    ser=models.IntegerField(null=True)
