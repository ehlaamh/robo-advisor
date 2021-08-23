from django.db import models

class Userreg(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    class Meta:
        db_table="user"