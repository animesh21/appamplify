# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-27 13:23
from __future__ import unicode_literals

from django.db import migrations


def add_instance_types(apps, schema_editor):
    InstanceTypeModel = apps.get_model('aws', 'AWSInstanceTypeModel')
    
    types = ['t1.micro', 't2.nano', 't2.micro', 't2.small', 't2.medium', 't2.large', 't2.xlarge', 't2.2xlarge', 'm1.small', 'm1.medium', 'm1.large', 'm1.xlarge', 'm3.medium', 'm3.large', 'm3.xlarge', 'm3.2xlarge', 'm4.large', 'm4.xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.10xlarge', 'm4.16xlarge', 'm2.xlarge', 'm2.2xlarge', 'm2.4xlarge', 'cr1.8xlarge', 'r3.large', 'r3.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'r4.large', 'r4.xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.16xlarge', 'x1.16xlarge', 'x1.32xlarge', 'i2.xlarge', 'i2.2xlarge', 'i2.4xlarge', 'i2.8xlarge', 'i3.large', 'i3.xlarge', 'i3.2xlarge', 'i3.4xlarge', 'i3.8xlarge', 'i3.16xlarge', 'hi1.4xlarge', 'hs1.8xlarge', 'c1.medium', 'c1.xlarge', 'c3.large', 'c3.xlarge', 'c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'c4.large', 'c4.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge', 'cc1.4xlarge', 'cc2.8xlarge', 'g2.2xlarge', 'g2.8xlarge', 'g3.4xlarge', 'g3.8xlarge', 'g3.16xlarge', 'cg1.4xlarge', 'p2.xlarge', 'p2.8xlarge', 'p2.16xlarge', 'd2.xlarge', 'd2.2xlarge', 'd2.4xlarge', 'd2.8xlarge', 'f1.2xlarge', 'f1.16xlarge',]

    for type_name in types:
        InstanceTypeModel.objects.create(name=type_name)


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0002_awsinstancetypemodel_awsspotinstancerequestmodel'),
    ]

    operations = [
        migrations.RunPython(add_instance_types),
    ]
