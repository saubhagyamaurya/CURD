from django.db import models
import datetime

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150,blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150,default='none')
    password = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'users'

class update(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=150, blank=True, null=True)


class delete(models.Model):
    user_id = models.IntegerField()

class single(models.Model):
    user_id = models.IntegerField()

    


