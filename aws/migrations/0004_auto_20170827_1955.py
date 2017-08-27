# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-27 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0003_auto_20170827_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='AWSSpotInstanceRequestID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_request', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='awsspotinstancerequestmodel',
            name='request_id',
        ),
        migrations.AddField(
            model_name='awsspotinstancerequestid',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aws_requests', to='aws.AWSSpotInstanceRequestModel'),
        ),
    ]
