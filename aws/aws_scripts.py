import os
import errno
import boto3
from datetime import datetime


def configure_aws(access_key, secret_key):
    # making the .aws directory if it doesn't exists
    try:
        os.mkdir(os.path.expanduser('~/.aws'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        pass

    with open(os.path.expanduser('~/.aws/credentials'), 'w') as f:
        f.writelines(['[default]\n',
                      'aws_access_key_id = {}\n'.format(access_key),
                      'aws_secret_access_key = {}\n'.format(secret_key)])

    with open(os.path.expanduser('~/.aws/config'), 'w') as f:
        f.writelines(['[default]\n', 'region=ap-south-1\n'])


def request_spot_fleet(num_instances, instance_type, spot_price, expiration_time):
    client = boto3.client('ec2')
    response = client.request_spot_fleet(
        DryRun=True,
        SpotFleetRequestConfig={
            'AllocationStrategy': 'lowestPrice',
            # 'ClientToken': 'string',
            # 'ExcessCapacityTerminationPolicy': 'noTermination' | 'default',
            'FulfilledCapacity': num_instances,  # 123.0,
            'IamFleetRole': 'terminateInstancesWithExpiration',
            'LaunchSpecifications': [
                {
                    # 'SecurityGroups': [
                    #     {
                    #         'GroupName': 'string',
                    #         'GroupId': 'string'
                    #     },
                    # ],
                    # 'AddressingType': 'string',
                    # 'BlockDeviceMappings': [
                    #     {
                    #         'DeviceName': 'string',
                    #         'VirtualName': 'string',
                    #         'Ebs': {
                    #             'Encrypted': True | False,
                    #             'DeleteOnTermination': True | False,
                    #             'Iops': 123,
                    #             'SnapshotId': 'string',
                    #             'VolumeSize': 123,
                    #             'VolumeType': 'standard' | 'io1' | 'gp2' | 'sc1' | 'st1'
                    #         },
                    #         'NoDevice': 'string'
                    #     },
                    # ],
                    # 'EbsOptimized': True | False,
                    # 'IamInstanceProfile': {
                    #     'Arn': 'string',
                    #     'Name': 'string'
                    # },
                    # 'ImageId': 'string',
                    'InstanceType': instance_type,  # 't1.micro' | 't2.nano' | 't2.micro' | 't2.small' | 't2.medium' | 't2.large' | 't2.xlarge' | 't2.2xlarge' | 'm1.small' | 'm1.medium' | 'm1.large' | 'm1.xlarge' | 'm3.medium' | 'm3.large' | 'm3.xlarge' | 'm3.2xlarge' | 'm4.large' | 'm4.xlarge' | 'm4.2xlarge' | 'm4.4xlarge' | 'm4.10xlarge' | 'm4.16xlarge' | 'm2.xlarge' | 'm2.2xlarge' | 'm2.4xlarge' | 'cr1.8xlarge' | 'r3.large' | 'r3.xlarge' | 'r3.2xlarge' | 'r3.4xlarge' | 'r3.8xlarge' | 'r4.large' | 'r4.xlarge' | 'r4.2xlarge' | 'r4.4xlarge' | 'r4.8xlarge' | 'r4.16xlarge' | 'x1.16xlarge' | 'x1.32xlarge' | 'i2.xlarge' | 'i2.2xlarge' | 'i2.4xlarge' | 'i2.8xlarge' | 'i3.large' | 'i3.xlarge' | 'i3.2xlarge' | 'i3.4xlarge' | 'i3.8xlarge' | 'i3.16xlarge' | 'hi1.4xlarge' | 'hs1.8xlarge' | 'c1.medium' | 'c1.xlarge' | 'c3.large' | 'c3.xlarge' | 'c3.2xlarge' | 'c3.4xlarge' | 'c3.8xlarge' | 'c4.large' | 'c4.xlarge' | 'c4.2xlarge' | 'c4.4xlarge' | 'c4.8xlarge' | 'cc1.4xlarge' | 'cc2.8xlarge' | 'g2.2xlarge' | 'g2.8xlarge' | 'g3.4xlarge' | 'g3.8xlarge' | 'g3.16xlarge' | 'cg1.4xlarge' | 'p2.xlarge' | 'p2.8xlarge' | 'p2.16xlarge' | 'd2.xlarge' | 'd2.2xlarge' | 'd2.4xlarge' | 'd2.8xlarge' | 'f1.2xlarge' | 'f1.16xlarge',
                    # 'KernelId': 'string',
                    # 'KeyName': 'string',
                    'Monitoring': {
                        'Enabled': True  # | False
                    },
                    # 'NetworkInterfaces': [
                    #     {
                    #         'AssociatePublicIpAddress': True | False,
                    #         'DeleteOnTermination': True | False,
                    #         'Description': 'string',
                    #         'DeviceIndex': 123,
                    #         'Groups': [
                    #             'string',
                    #         ],
                    #         'Ipv6AddressCount': 123,
                    #         'Ipv6Addresses': [
                    #             {
                    #                 'Ipv6Address': 'string'
                    #             },
                    #         ],
                    #         'NetworkInterfaceId': 'string',
                    #         'PrivateIpAddress': 'string',
                    #         'PrivateIpAddresses': [
                    #             {
                    #                 'Primary': True | False,
                    #                 'PrivateIpAddress': 'string'
                    #             },
                    #         ],
                    #         'SecondaryPrivateIpAddressCount': 123,
                    #         'SubnetId': 'string'
                    #     },
                    # ],
                    # 'Placement': {
                    #     'AvailabilityZone': 'string',
                    #     'GroupName': 'string',
                    #     'Tenancy': 'default' | 'dedicated' | 'host'
                    # },
                    # 'RamdiskId': 'string',
                    # 'SpotPrice': 'string',
                    # 'SubnetId': 'string',
                    # 'UserData': 'string',
                    'WeightedCapacity': 123.0,
                    # 'TagSpecifications': [
                    #     {
                    #         'ResourceType': 'customer-gateway' | 'dhcp-options' | 'image' | 'instance' | 'internet-gateway' | 'network-acl' | 'network-interface' | 'reserved-instances' | 'route-table' | 'snapshot' | 'spot-instances-request' | 'subnet' | 'security-group' | 'volume' | 'vpc' | 'vpn-connection' | 'vpn-gateway',
                    #         'Tags': [
                    #             {
                    #                 'Key': 'string',
                    #                 'Value': 'string'
                    #             },
                    #         ]
                    #     },
                    # ]
                },
            ],
            'SpotPrice': str(spot_price),
            'TargetCapacity': num_instances,  # 123,
            'TerminateInstancesWithExpiration': True,  # | False,
            'Type': 'maintain',  # 'request' | 'maintain',
            # 'ValidFrom': datetime(2015, 1, 1),
            'ValidUntil': datetime.now() + expiration_time,
            'ReplaceUnhealthyInstances': True  # | False
        }
    )
    return response
