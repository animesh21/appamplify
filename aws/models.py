from django.db import models
from django.contrib.auth.models import User
from .aws_scripts import configure_aws, request_spot_fleet


class AWSInstanceModel(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    login_name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=16)
    port_number = models.IntegerField(default=22)
    key = models.FileField(upload_to='keys/')
    password = models.CharField(max_length=256)

    def __str__(self):
        return '<User: {}, name: {}>'.format(self.user.username, self.name)


class AWSCredentialsModel(models.Model):
    user = models.OneToOneField(User)
    access_key = models.CharField(max_length=20)
    secret_key = models.CharField(max_length=40)

    def configure(self):
        configure_aws(access_key=self.access_key, secret_key=self.secret_key)

    def __str__(self):
        return '<Credentials for the user: {}>'.format(self.user.username)


class AWSInstanceTypeModel(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class AWSSpotInstanceRequestModel(models.Model):
    user = models.ForeignKey(User)
    num_instances = models.IntegerField(null=True, default=None, verbose_name='Number of Instances')
    instance_type = models.ForeignKey('AWSInstanceTypeModel')
    max_price = models.FloatField(null=True, default=None)
    expiration_time = models.DurationField()
    # request_id = models.CharField(max_length=255, null=True, default=None)

    def request_fleet(self):
        res = request_spot_fleet(
            self.num_instances,
            self.instance_type.name,
            str(self.max_price),
            self.expiration_time
        )
        for spot_request in res.get('SpotInstanceRequests', []):
            AWSSpotInstanceRequestID.objects.create(
                request_id=spot_request['SpotInstanceRequestId'],
                request=self
            )

    def __str__(self):
        return '<AWS Spot Instance Request: {}>'.format(', '.join(list(self.aws_requests)))


class AWSSpotInstanceRequestID(models.Model):
    spot_request = models.CharField(max_length=255)
    request = models.ForeignKey('AWSSpotInstanceRequestModel', related_name='aws_requests')
