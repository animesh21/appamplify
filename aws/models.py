from django.db import models
from django.contrib.auth.models import User


class AWSInstanceModel(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    login_name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=16)
    port_number = models.IntegerField(default=22)
    key = models.FileField(upload_to='keys/')
    password = models.CharField(max_length=256)
