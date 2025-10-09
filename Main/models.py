from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=20)
    user_pass = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=12)
    user_email = models.CharField(max_length=50)
    user_complains = models.IntegerField()

    def __str__(self):
        return self.user_name
class Worker(models.Model):
    worker_id = models.AutoField
    worker_name = models.CharField(max_length=20)
    worker_pass = models.CharField(max_length=30)
    worker_phone = models.CharField(max_length=12)
    worker_email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.worker_name    

class Complain(models.Model):
    complain_id = models.AutoField
    domain_name = models.CharField(max_length=20,default='idc')
    user_name = models.CharField(max_length=30,default='idc')
    status = models.CharField(max_length=12,default='Pending')
    info = models.CharField(max_length=500,default='idc')
    landmark = models.CharField(max_length=50,default='idc')
    image = models.ImageField(upload_to="Main/images",default="")
    locx = models.CharField(max_length=20,default='0')
    locy = models.CharField(max_length=20,default='0')
    
    def __str__(self):
        return self.location