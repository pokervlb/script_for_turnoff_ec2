import boto3

# create connection with AWS
ec2 = boto3.client('ec2', region_name='eu-west-1',
                   aws_access_key_id='your_access_key',
                   aws_secret_access_key='your_secret_access_key')


response = ec2.describe_instances()

# shutdown running instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
            ec2.stop_instances(InstanceIds=[instance['InstanceId']])
            print(f"Instance {instance['InstanceId']} stopped.")

