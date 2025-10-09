from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=20)
    user_pass = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=12)
    user_email = models.CharField(max_length=50)
    user_complains = models.IntegerField()
    
class Worker(models.Model):
    worker_id = models.AutoField
    worker_name = models.CharField(max_length=20)
    worker_pass = models.CharField(max_length=30)
    worker_phone = models.CharField(max_length=12)
    worker_email = models.CharField(max_length=50)
    
